from copy import deepcopy
from typing import List, Dict
import json
from ProAgent.frontend.highlight_code import highlight_code
from ProAgent.running_recorder import RunningRecoder

from ProAgent.handler import react_prompt
from ProAgent.utils import userQuery, Action
from ProAgent.agent.gpt4_function import OpenAIFunction
from ProAgent.n8n_parser.compiler import Compiler
from ProAgent.loggers.logs import logger
from ProAgent.n8n_parser.intrinsic_functions import get_intrinsic_functions
from ProAgent.config import CONFIG

class ReACTHandler():
    def __init__(self, cfg, query:userQuery, compiler: Compiler, recorder: RunningRecoder, refine_oneshot_data=None):
        """
        Initializes a new instance of the class.

        Args:
            cfg (type): The cfg parameter description.
            query (userQuery): The query parameter description.
            compiler (Compiler): The compiler parameter description.
            recorder (RunningRecoder): The recorder parameter description.
            refine_oneshot_data (dict, optional): Data for refine_oneshot mode containing old query and workflow.
                Should have keys: 'old_query' (userQuery), 'workflow_code' (str)

        Attributes:
            messages (List[Dict]): The messages attribute description.
            actions (List[Action]): The actions attribute description.
        """
        self.query = query
        self.refine_prompt = query.refine_prompt
        self.cfg = cfg
        self.compiler = compiler
        self.recorder = recorder
        self.messages: List[Dict] = []
        self.actions: List[Action] = []
        self.refine_oneshot_data = refine_oneshot_data
    def run(self):
        """
        Runs the main loop for the program.

        This function continuously executes a loop that performs the following steps:
        1. Appends system prompts to the list of messages.
        2. Replaces placeholders in a specific prompt and appends it to the list of messages.
        3. Appends assistant messages and function outputs to the list of messages.
        4. Prints highlighted code.
        5. Replaces placeholders in the user prompt and appends it to the list of messages.
        6. Retrieves intrinsic functions.
        7. Parses messages using an OpenAIFunction agent.
        8. Handles tool calls using the compiler.
        9. Appends the parsed message and action to the list of messages and actions, respectively.

        This function does not have any parameters and does not return anything.

        Note: This function runs indefinitely until interrupted.
        """
        while True:
            messages = []
            messages.append({"role":"system","content": deepcopy(react_prompt.system_prompt_1)})
            messages.append({"role":"system","content": deepcopy(react_prompt.system_prompt_2)})

            specific_prompt = deepcopy(react_prompt.system_prompt_3)
            specific_prompt = specific_prompt.replace("{{user_query}}", self.query.print_self())
            specific_prompt = specific_prompt.replace("{{flatten_tools}}", self.compiler.print_flatten_tools())
            messages.append({"role":"system","content": specific_prompt})

            # Inject refine_oneshot reference workflow if provided
            if self.refine_oneshot_data is not None and len(self.messages) == 0:
                # Only inject on first iteration
                old_query = self.refine_oneshot_data.get('old_query')
                workflow_code = self.refine_oneshot_data.get('workflow_code', '')

                if old_query and workflow_code:
                    refine_oneshot_prompt = f"""
🔄 REFINE_ONESHOT MODE - INCREMENTAL WORKFLOW UPDATE

IMPORTANT: The reference workflow from ID_{old_query.ID} has ALREADY BEEN LOADED into the compiler.
All trigger and action nodes from the reference workflow are already defined and configured in the system.
You should treat this as an INCREMENTAL UPDATE task, not a from-scratch implementation.

═══════════════════════════════════════════════════════════════

⚠️ STEP 0: FIRST, IDENTIFY ALL DIFFERENCES LINE-BY-LINE ⚠️

Compare these two queries carefully. Look for ANY text that changed:

REFERENCE QUERY (ID: {old_query.ID}):
{old_query.print_self()}

CURRENT/NEW QUERY (ID: {self.query.ID}):
{self.query.print_self()}

Before proceeding, write down EVERY difference you found:
- Which line numbers differ between reference and new query?
- What values changed? (e.g., "commercial" → "commercial-small", "#general" → "#news")
- Which function parameters need updating based on these changes?

═══════════════════════════════════════════════════════════════

REFERENCE WORKFLOW CODE (for understanding only):
The following code shows the final successful implementation for the reference query.
Study it to understand the workflow structure and logic.

```python
{workflow_code}
```

═══════════════════════════════════════════════════════════════

YOUR TASK - INCREMENTAL UPDATE STRATEGY:

⚠️  CRITICAL: The reference workflow nodes are ALREADY LOADED. DO NOT redefine functions!

Step 1: ANALYZE the differences CAREFULLY (line-by-line comparison!)
   - ⚠️ DO NOT SKIP THIS: Compare EVERY line of additional_information between queries
   - Look at each numbered item (1.1, 1.2, 4.2, etc.) and check if the text changed
   - Common changes to look for:
     * Sheet/file names (e.g., "commercial" vs "commercial-small")
     * Channel names (e.g., "#general" vs "#news")
     * Email addresses
     * URLs, IDs, file paths
     * Logic changes (filtering, conditions)

   Example comparison process:
   Reference line: "4.2 Send results to slack channel #general"
   New line:       "4.2 Send results to slack channel #news"
   → DIFFERENCE FOUND: Slack channel changed from "general" to "news"
   → ACTION NEEDED: Update action_2 (slack) channelId parameter

   ⚠️ CRITICAL: Write ALL changes in your "thought" field as a TODO checklist!
   - Format: "TODO: [all remaining tasks]. DONE: [completed tasks]. Now doing: [current]"
   - This ensures you don't forget any changes across iterations

   Example thought progression for 2 changes:
   Iteration 1: "TODO: Update action_0 sheetName to 'commercial-small', Update action_2 channelId to 'news'. DONE: None. Now doing: Update action_0."
   Iteration 2: "TODO: Update action_2 channelId to 'news'. DONE: action_0 sheetName. Now doing: Update action_2."
   Iteration 3: "TODO: None. DONE: action_0 sheetName, action_2 channelId. Now doing: Submit task."

   ⚠️ CRITICAL: Count how many changes you identified. You will need ONE tool call per change!
   If you identify 2 parameter changes, you need 2 function_rewrite_params calls (one per iteration).
   ALWAYS repeat your TODO list in the "thought" field so you remember what's left!

Step 2: UPDATE existing nodes ONE AT A TIME (preferred approach)
   - Use function_rewrite_params to update parameters of existing actions/triggers
   - ⚠️ Make ONLY ONE tool call per iteration - you cannot update multiple functions at once!
   - After each update, check your plan to see what's left to do
   - Continue making function_rewrite_params calls until all parameters are updated
   - Only change the specific parameters that differ between queries
   - Example: If only the sheet name changed from 'commercial' to 'commercial-small':
     → Call function_rewrite_params for action_0 to update the sheetName parameter
     → DO NOT redefine action_0 entirely

Step 3: REWRITE mainWorkflow only if logic changed
   - If the NEW QUERY requires different workflow logic (different data processing, new conditions, etc.):
     → Use workflow_implment to rewrite ONLY the mainWorkflow function
     → The mainWorkflow should CALL the existing action functions (action_0, action_1, etc.)
     → DO NOT include action/trigger function definitions in the workflow_implment code
   - If the workflow logic is the same and only parameters changed:
     → No need to rewrite mainWorkflow at all

EXAMPLES OF CORRECT APPROACH:

Example 1 - Multiple parameter changes (MULTI-STEP PROCESS):
  Reference Query: Read from sheet 'commercial', send to slack channel #general
  New Query: Read from sheet 'commercial-small', send to slack channel #general-test

  Analysis of changes:
  - action_0 (googleSheets): sheetName 'commercial' → 'commercial-small'
  - action_2 (slack): channelId 'general' → 'general-test'
  - mainWorkflow: No logic changes needed

  ⚠️ IMPORTANT: You can only make ONE tool call per iteration!
  After each tool call, you will see the result and can make the next call.

  ✅ Correct approach (iterative process):
    Iteration 1:
      Thought: "TODO: Update action_0 sheetName, Update action_2 channelId. DONE: None. Now doing: Update action_0 sheetName from 'commercial' to 'commercial-small'."
      Tool Call: function_rewrite_params for action_0 (update sheetName to 'commercial-small')

    Iteration 2 (after seeing action_0 updated successfully):
      Thought: "TODO: Update action_2 channelId. DONE: action_0 sheetName. Now doing: Update action_2 channelId from 'general' to 'general-test'."
      Tool Call: function_rewrite_params for action_2 (update channelId to 'general-test')

    Iteration 3 (after seeing action_2 updated successfully):
      Thought: "TODO: None. DONE: action_0 sheetName, action_2 channelId. Now doing: Submit completed workflow."
      Tool Call: task_submit

  ❌ Wrong approach:
    - Iteration 1: Update action_0, then immediately task_submit (forgetting action_2!)
    - Redefining all functions with workflow_implment instead of targeted updates
    - Thinking you can make multiple tool calls in one iteration

Example 2 - Logic change:
  Reference: Classify entries and send to slack OR email
  New: Classify entries, filter by cost>5000, and send only high-value entries
  ✅ Correct: Update mainWorkflow with new filtering logic, call existing actions
  ❌ Wrong: Redefine action functions that don't need changes

RULES:
1. Existing trigger/action functions are already defined - reference them by name (trigger_0, action_0, etc.)
2. Use function_rewrite_params for parameter-only updates (most efficient)
3. Use workflow_implment ONLY for mainWorkflow if logic needs to change
4. When using workflow_implment, write ONLY the mainWorkflow function definition
5. Pay attention to small changes like: 'commercial' → 'commercial-small', '#general' → '#general-test'
6. Minimize changes - only update what's different between the queries

Start by analyzing what changed between the reference and new queries, then choose the appropriate tool calls.
"""
                    messages.append({"role":"user","content": refine_oneshot_prompt})
                else:
                    assert False
            else:
                # cut some messages down, only allow for last_num messages
                messages.append({"role": "system", "content": "In the following messages, three previous assistant response with tool output are given."})
                last_num = 5
                for k, (assistant_message, parsed_action) in enumerate(zip(self.messages, self.actions)):
                    if k < len(self.messages) - last_num:
                        continue
                    if assistant_message != None:
                        messages.append(assistant_message)
                    messages.append({
                        # "role":"function",
                        "role": "user",
                        # "name": parsed_action.tool_name,
                        "content": parsed_action.tool_output,
                    })


                user_prompt = deepcopy(react_prompt.user_prompt)

                refine_prompt = ""
                if len(self.refine_prompt) > 0:
                    refine_prompt = f"The user have some additional requirements to your work. Please refine your work based on the following requirements:\n ```\n{deepcopy(self.refine_prompt)}```\n"

                user_prompt = user_prompt.replace("{{refine_prompt}}", refine_prompt)

                # print highlighted code
                highlighted_code = highlight_code(self.compiler.code_runner.print_clean_code(indent=4))
                user_prompt_colored = user_prompt.split("{{now_codes}}")
                user_prompt_colored = highlighted_code.join(user_prompt_colored)
                # logger.typewriter_log(user_prompt_colored)

                user_prompt = user_prompt.replace("{{now_codes}}", self.compiler.code_runner.print_code())

                messages.append({"role":"user","content": user_prompt})
            
            functions = get_intrinsic_functions()

            agent = OpenAIFunction()
            # call agent, query cached llm inout (if you want to load previous llm result)
            # save llm inout result (LLM_inout_pair)
            content, function_name, function_arguments, message = agent.parse(messages=messages,
                                                            functions=functions,
                                                            default_completion_kwargs=CONFIG.default_completion_kwargs,
                                                            recorder=self.recorder)

            # run code
            # function_name => tool_name
            # function_arguments => tool_input
            action = self.compiler.tool_call_handle(content, function_name, function_arguments)
            self.messages.append(message)
            self.actions.append(action)

            if action.tool_name == 'ask_user_help':
                print('ask_user_help exit!!!')
                # exit()
            elif action.tool_name == 'task_submit':
                print('task_submit finish!!!')
                break # break while
            # exit()