"""
Enhanced Gemini Agent for ProAgent with Direct Message Enhancement
Fixes function calling issues by enhancing user messages directly
Updated with aggressive message enhancement to force proper function calling
"""

import os
import json
from typing import Dict, List, Optional, Union, Tuple
import google.generativeai as genai
from google.generativeai.types import Tool, FunctionDeclaration

class GeminiChatCompletion:
    def __init__(self):
        # Configure Gemini API
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        
        # Safety settings
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]

    def get_model_name(self, openai_model: str) -> str:
        """Map OpenAI model names to Gemini model names"""
        # Check environment variable override FIRST
        env_override = os.getenv('GEMINI_MODEL_OVERRIDE')
        if env_override:
            return f'models/{env_override}'
        
        # Check for API_PROVIDER=gemini-flash
        api_provider = os.getenv('API_PROVIDER', '')
        if api_provider == 'gemini-flash':
            return 'models/gemini-2.0-flash-exp'  # Force Flash model
        
        # Model mapping
        MODEL_MAPPING = {
            'gpt-4': 'models/gemini-2.0-flash-exp',
            'gpt-4-turbo': 'models/gemini-2.0-flash-exp', 
            'gpt-3.5-turbo': 'models/gemini-2.0-flash-exp',
            'gpt-4-0613': 'models/gemini-2.0-flash-exp',
            'gpt-4-turbo-preview': 'models/gemini-2.0-flash-exp'
        }
        
        return MODEL_MAPPING.get(openai_model, 'models/gemini-2.0-flash-exp')

    def convert_messages(self, messages: List[Dict]) -> Tuple[List[Dict], str]:
        """Convert OpenAI messages to Gemini format"""
        converted_messages = []
        system_instruction = None
        
        for message in messages:
            role = message['role']
            content = message['content']
            
            if role == 'system':
                system_instruction = content
            elif role in ['user', 'assistant']:
                converted_messages.append({
                    'role': 'user' if role == 'user' else 'model',
                    'parts': [content]
                })
        
        # ENHANCED SYSTEM INSTRUCTION
        if system_instruction:
            enhanced_system = f"""{system_instruction}

CRITICAL FUNCTION CALLING INSTRUCTIONS:
When calling functions, you must provide ACTUAL IMPLEMENTATION VALUES, not schema field names.

For function_define calls specifically:
- integration_name: Use actual integration names like "googleSheets", "manualTrigger", "aiCompletion" 
- resource_name: Use actual node names like "Trigger_1", "Action_1", "Action_2"
- operation_name: Use actual operations like "default", "sheet.read", "default.default"
- comments: Write actual descriptive text in Chinese explaining the node's purpose
- TODO: Provide actual actionable implementation tasks as strings

You are a workflow designer providing real configuration values, not a schema validator returning field templates.

Example of CORRECT function calling:
{{
  "integration_name": "googleSheets",
  "resource_name": "Action_1", 
  "operation_name": "sheet.read",
  "comments": "从Google表格读取业务数据",
  "TODO": ["设置documentId参数", "设置sheetName参数"]
}}

WRONG (do not do this):
["integration_name", "resource_name", "operation_name", "comments", "TODO"]"""
        else:
            enhanced_system = """CRITICAL FUNCTION CALLING INSTRUCTIONS:
When calling functions, provide ACTUAL VALUES, not field names. Think like a workflow designer configuring real n8n nodes."""
        
        return converted_messages, enhanced_system

    def convert_property_type(self, prop_def: Dict) -> Dict:
        """Convert OpenAI property definition to Gemini format"""
        prop_type = prop_def.get('type', 'string').lower()
        converted_prop = {}
        
        # Copy description if present
        if 'description' in prop_def:
            converted_prop['description'] = prop_def['description']
        
        if prop_type == 'string':
            converted_prop['type'] = 'STRING'
        elif prop_type == 'number':
            converted_prop['type'] = 'NUMBER'
        elif prop_type == 'integer':
            converted_prop['type'] = 'INTEGER'
        elif prop_type == 'boolean':
            converted_prop['type'] = 'BOOLEAN'
        elif prop_type == 'array':
            converted_prop['type'] = 'ARRAY'
            
            # Handle array items
            if 'items' in prop_def:
                items_def = prop_def['items']
                if isinstance(items_def, dict):
                    converted_prop['items'] = self.convert_property_type(items_def)
                else:
                    # Simple type
                    converted_prop['items'] = {'type': 'STRING'}
            else:
                converted_prop['items'] = {'type': 'STRING'}
                
        elif prop_type == 'object':
            converted_prop['type'] = 'OBJECT'
            
            # Handle object properties
            if 'properties' in prop_def:
                converted_prop['properties'] = {}
                for obj_prop_name, obj_prop_def in prop_def['properties'].items():
                    converted_prop['properties'][obj_prop_name] = self.convert_property_type(obj_prop_def)
        else:
            # Default to string for unknown types
            converted_prop['type'] = 'STRING'
        
        return converted_prop
    
    def convert_functions(self, functions: List[Dict]) -> List:
        """
        Convert OpenAI function schema to Gemini function declarations
        Enhanced with explicit instructions for function_define
        """
        if not functions:
            return None
        
        from google.generativeai.types import Tool, FunctionDeclaration
        
        function_declarations = []
        
        for func in functions:
            try:
                # Get function info
                func_name = func['name']
                base_description = func.get('description', '')

                # Add explicit instructions for function_define to prevent field name returns
                if func_name == 'function_define':
                    func_description = f"""{base_description}

CRITICAL: When calling this function, you must provide ACTUAL VALUES for each field, not field names.

Examples:
- integration_name: "googleSheets" (NOT "integration_name") 
- resource_name: "Action_1" (NOT "resource_name")
- operation_name: "sheet.read" (NOT "operation_name")
- comments: "Read business data from Google Sheets" (NOT "comments")
- TODO: ["Set documentId parameter", "Set sheetName parameter"] (NOT ["TODO"])

Provide complete objects with real values that can be used to configure n8n nodes."""
                else:
                    func_description = base_description

                parameters = func.get('parameters', {})
                
                # Convert parameters schema
                converted_parameters = {}
                
                if 'properties' in parameters:
                    converted_parameters['type'] = 'OBJECT'
                    converted_parameters['properties'] = {}
                    
                    # Convert each property
                    for prop_name, prop_def in parameters['properties'].items():
                        converted_parameters['properties'][prop_name] = self.convert_property_type(prop_def)
                    
                    # Handle required fields
                    if 'required' in parameters:
                        converted_parameters['required'] = parameters['required']
                
                # Create function declaration
                func_decl = FunctionDeclaration(
                    name=func_name,
                    description=func_description,
                    parameters=converted_parameters
                )
                function_declarations.append(func_decl)
                
            except Exception as e:
                print(f"Warning: Failed to convert function {func.get('name', 'unknown')}: {e}")
                # Skip problematic functions rather than failing entirely
                continue
        
        if not function_declarations:
            return None
            
        return [Tool(function_declarations=function_declarations)]

    def create_completion(self, model: str, messages: List[Dict],
                          functions: Optional[List[Dict]] = None,
                          function_call: Optional[Union[str, Dict]] = None,
                          temperature: float = 0.5,
                          max_tokens: int = 4096,
                          **kwargs) -> Dict:
        try:
            # Map model name
            gemini_model = self.get_model_name(model)

            # Convert messages and functions
            converted_messages, system_instruction = self.convert_messages(messages)
            tools = self.convert_functions(functions) if functions else None

            # DEBUG: Print what we're actually sending
            print("=== SYSTEM INSTRUCTION DEBUG ===")
            print(f"System instruction length: {len(system_instruction) if system_instruction else 0}")
            if system_instruction:
                print(f"System instruction (first 200 chars): {system_instruction[:200]}...")
                print(f"Contains 'CRITICAL FUNCTION CALLING': {'CRITICAL FUNCTION CALLING' in system_instruction}")
            else:
                print("No system instruction found!")
            print("=== END SYSTEM DEBUG ===")

            # ENHANCED GENERATION CONFIG
            generation_config = {
                'temperature': 0.0,  # Completely deterministic
                'max_output_tokens': max_tokens,
                'top_p': 0.1,  # Very focused generation
                'top_k': 40  # Add top_k for more predictable choices
            }

            # Create model instance with function calling mode ANY
            model_instance = genai.GenerativeModel(
                model_name=gemini_model,
                generation_config=generation_config,
                safety_settings=self.safety_settings,
                system_instruction=system_instruction,
                tools=tools
            )

            # Start chat with function calling mode ANY
            if len(converted_messages) > 1:
                history = converted_messages[:-1]
                current_message = converted_messages[-1]['parts'][0]
                
                # DIRECT MESSAGE ENHANCEMENT - Add instructions directly to user message
                if tools and any('function_define' in str(tool) for tool in tools):
                    enhanced_message = f"""{current_message}

🚨 CRITICAL REMINDER: When calling function_define, provide ACTUAL VALUES:
- integration_name: "manualTrigger" or "googleSheets" (NOT "integration_name")
- resource_name: "Trigger_1" or "Action_1" (NOT "resource_name") 
- operation_name: "default" or "sheet.read" (NOT "operation_name")
- comments: Real Chinese descriptions (NOT "comments")
- TODO: Actual task strings (NOT ["TODO"])

Configure real n8n nodes with actual values, not schema templates.

Example correct response:
{{
  "functions": [
    {{
      "integration_name": "manualTrigger",
      "resource_name": "Trigger_1",
      "operation_name": "default",
      "comments": "手动启动工作流程",
      "TODO": ["配置触发器参数", "测试触发功能"]
    }},
    {{
      "integration_name": "googleSheets", 
      "resource_name": "Action_1",
      "operation_name": "sheet.read",
      "comments": "从Google表格读取数据",
      "TODO": ["设置documentId参数", "设置sheetName参数"]
    }}
  ]
}}"""
                    current_message = enhanced_message
                    print(f"🔧 Enhanced user message with direct function calling instructions")

                chat = model_instance.start_chat(history=history)

                # KEY FIX: Add tool_config with function calling mode ANY
                tool_config = None
                if tools:
                    tool_config = {
                        'function_calling_config': {
                            'mode': 'ANY'  # Enable constrained decoding
                        }
                    }

                response = chat.send_message(
                    current_message,
                    generation_config=generation_config,
                    safety_settings=self.safety_settings,
                    tools=tools,
                    tool_config=tool_config
                )
            else:
                current_message = converted_messages[0]['parts'][0] if converted_messages else ""

                # DIRECT MESSAGE ENHANCEMENT for single message too
                if tools and any('function_define' in str(tool) for tool in tools):
                    enhanced_message = f"""{current_message}

🚨 CRITICAL: Provide ACTUAL VALUES in function_define, not field names.
Use real integration names like "manualTrigger", "googleSheets", real resource names like "Trigger_1", "Action_1".

Do NOT return arrays like ["integration_name", "resource_name"] - return objects with actual values."""
                    current_message = enhanced_message
                    print(f"🔧 Enhanced single message with function calling instructions")

                # For single message, also add tool_config
                tool_config = None
                if tools:
                    tool_config = {
                        'function_calling_config': {
                            'mode': 'ANY'
                        }
                    }

                response = model_instance.generate_content(
                    current_message,
                    generation_config=generation_config,
                    safety_settings=self.safety_settings,
                    tools=tools,
                    tool_config=tool_config
                )

            return self.convert_response(response)

        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")

    def _convert_protobuf_value(self, value):
        """Convert protobuf value to Python native type with better handling"""
        try:
            # Handle different protobuf value types
            if hasattr(value, 'string_value'):
                return value.string_value
            elif hasattr(value, 'number_value'):
                return value.number_value
            elif hasattr(value, 'bool_value'):
                return value.bool_value
            elif hasattr(value, 'list_value'):
                result = []
                for item in value.list_value.values:
                    result.append(self._convert_protobuf_value(item))
                return result
            elif hasattr(value, 'struct_value'):
                result = {}
                for k, v in value.struct_value.fields.items():
                    result[k] = self._convert_protobuf_value(v)
                return result
            else:
                # Handle MapComposite and RepeatedComposite from proto.marshal
                if hasattr(value, '__iter__') and not isinstance(value, str):
                    try:
                        # Try to iterate as list
                        return [self._convert_protobuf_value(item) for item in value]
                    except:
                        try:
                            # Try to iterate as dict
                            return {k: self._convert_protobuf_value(v) for k, v in value.items()}
                        except:
                            return str(value)
                
                return str(value)
                
        except Exception as e:
            print(f"Warning: Error converting protobuf value: {e}")
            return str(value)

    def convert_response(self, response) -> Dict:
        """Convert Gemini response to OpenAI-compatible format"""
        try:
            content = None
            function_call = None

            # Check for parts first
            if hasattr(response, 'parts') and response.parts:
                part = response.parts[0]

                if hasattr(part, 'function_call') and part.function_call:
                    # Convert function call with debugging
                    print("=== DETAILED FUNCTION DEBUG ===")
                    print(f"Function name: {part.function_call.name}")
                    print(f"Raw args type: {type(part.function_call.args)}")
                    
                    func_args = {}
                    for key, value in part.function_call.args.items():
                        converted_value = self._convert_protobuf_value(value)
                        print(f"Key '{key}':")
                        print(f"  Raw type: {type(value)}")
                        print(f"  Converted type: {type(converted_value)}")
                        print(f"  Converted value: {converted_value}")
                        func_args[key] = converted_value

                    print(f"Final func_args: {func_args}")
                    print("=== END DEBUG ===")
                    
                    function_call = {
                        'name': part.function_call.name,
                        'arguments': json.dumps(func_args)
                    }
                    # IMPORTANT: OpenAI function calls usually have empty content
                    content = ""  # Ensure content exists for compatibility

                elif hasattr(part, 'text'):
                    content = part.text

            # Fallback
            if content is None and function_call is None:
                content = ""

            # Build OpenAI-compatible message
            message = {
                'role': 'assistant',
                'content': content  # Always include content field
            }

            if function_call:
                message['function_call'] = function_call

            # Token usage calculation
            prompt_tokens = 0
            completion_tokens = len(content.split()) if content else 0

            if hasattr(response, 'usage_metadata'):
                prompt_tokens = getattr(response.usage_metadata, 'prompt_token_count', prompt_tokens)
                completion_tokens = getattr(response.usage_metadata, 'candidates_token_count', completion_tokens)

            return {
                'choices': [{
                    'message': message,
                    'finish_reason': 'function_call' if function_call else 'stop'
                }],
                'usage': {
                    'prompt_tokens': prompt_tokens,
                    'completion_tokens': completion_tokens,
                    'total_tokens': prompt_tokens + completion_tokens
                }
            }

        except Exception as e:
            raise Exception(f"Response conversion error: {str(e)}")


# Global function for backwards compatibility
def gemini_chat_completion_create(**kwargs):
    """Create a Gemini chat completion"""
    client = GeminiChatCompletion()
    return client.create_completion(**kwargs)
