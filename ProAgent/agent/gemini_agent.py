'''
Fixed Gemini Agent for ProAgent 
Properly handles complex function schemas with arrays
'''

import os
import json
from typing import Dict, List, Union, Optional, Any
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


# Model mapping
MODEL_MAPPING = {
    'gpt-4': 'models/gemini-2.5-pro',
    'gpt-4-turbo': 'models/gemini-2.5-pro', 
    'gpt-4-0613': 'models/gemini-2.5-pro',
    'gpt-3.5-turbo': 'models/gemini-2.5-flash',
}

# Model override mapping 
MODEL_OVERRIDE_MAPPING = {
    'gemini-2.5-flash': 'models/gemini-2.5-flash',
    'gemini-2.5-pro': 'models/gemini-2.5-pro',
    'gemini-flash': 'models/gemini-2.5-flash',
    'gemini-pro': 'models/gemini-2.5-pro'
}


class GeminiLLMClient:
    """
    Enhanced Gemini client with OpenAI-compatible interface
    Fixed array schema handling for ProAgent function calling
    """
    
    def __init__(self, api_key: str = None):
        # Configure Gemini
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        
        # Safety settings for research use
        self.safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    
    def get_model_name(self, openai_model: str) -> str:
        """Map OpenAI model name to Gemini model with config override support"""
        # Check for model override from config
        try:
            from ProAgent.config import CONFIG
            if hasattr(CONFIG, 'gemini_model_override') and CONFIG.gemini_model_override:
                override_model = CONFIG.gemini_model_override
                return MODEL_OVERRIDE_MAPPING.get(override_model, f'models/{override_model}')
        except:
            pass
        
        # Check environment variable override
        env_override = os.getenv('GEMINI_MODEL_OVERRIDE')
        if env_override:
            return MODEL_OVERRIDE_MAPPING.get(env_override, f'models/{env_override}')
        
        # Default mapping
        return MODEL_MAPPING.get(openai_model, 'models/gemini-2.5-pro')
    
    def convert_messages(self, messages: List[Dict]) -> List[Dict]:
        """Convert OpenAI message format to Gemini format"""
        converted_messages = []
        system_instruction = None
        
        for message in messages:
            role = message['role']
            content = message['content']
            
            if role == 'system':
                system_instruction = content
            elif role == 'user':
                converted_messages.append({
                    'role': 'user',
                    'parts': [content]
                })
            elif role == 'assistant':
                converted_messages.append({
                    'role': 'model', 
                    'parts': [content]
                })
            elif role == 'function':
                # Handle function results
                converted_messages.append({
                    'role': 'function',
                    'parts': [content]
                })
        
        return converted_messages, system_instruction
    
    def convert_property_type(self, prop_def: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert a single property definition from OpenAI to Gemini format
        Handles nested structures and arrays properly
        """
        converted_prop = prop_def.copy()
        
        # Convert type
        prop_type = prop_def.get('type', 'string')
        
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
            
            # Handle array items - CRITICAL FIX!
            if 'items' in prop_def:
                items_def = prop_def['items']
                
                # If items has a type, convert it
                if 'type' in items_def:
                    converted_items = self.convert_property_type(items_def)
                    converted_prop['items'] = converted_items
                elif 'properties' in items_def:
                    # Array of objects
                    converted_prop['items'] = {
                        'type': 'OBJECT',
                        'properties': {}
                    }
                    
                    # Convert each property in the object
                    for item_prop_name, item_prop_def in items_def['properties'].items():
                        converted_prop['items']['properties'][item_prop_name] = self.convert_property_type(item_prop_def)
                else:
                    # Default to string array if no items specified
                    converted_prop['items'] = {'type': 'STRING'}
            else:
                # Default array items if not specified
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
        Fixed to properly handle complex nested schemas and arrays
        """
        if not functions:
            return None
        
        from google.generativeai.types import Tool, FunctionDeclaration
        
        function_declarations = []
        
        for func in functions:
            try:
                # Get function info
                func_name = func['name']
                func_description = func.get('description', '')
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
        """Create a chat completion using Gemini API with OpenAI-compatible interface"""
        try:
            # Map model name
            gemini_model = self.get_model_name(model)
            
            # Convert messages
            converted_messages, system_instruction = self.convert_messages(messages)
            
            # Convert functions with improved schema handling
            tools = self.convert_functions(functions) if functions else None
            
            # Create model instance
            generation_config = {
                'temperature': temperature,
                'max_output_tokens': max_tokens,
            }
            
            model_instance = genai.GenerativeModel(
                model_name=gemini_model,
                generation_config=generation_config,
                safety_settings=self.safety_settings,
                system_instruction=system_instruction,
                tools=tools
            )
            
            # Start chat if we have conversation history
            if len(converted_messages) > 1:
                # Remove the last message (current user input)
                history = converted_messages[:-1]
                current_message = converted_messages[-1]['parts'][0]
                
                chat = model_instance.start_chat(history=history)
                response = chat.send_message(
                    current_message,
                    generation_config=generation_config,
                    safety_settings=self.safety_settings
                )
            else:
                # Single message
                current_message = converted_messages[0]['parts'][0] if converted_messages else ""
                response = model_instance.generate_content(
                    current_message,
                    generation_config=generation_config,
                    safety_settings=self.safety_settings
                )
            
            # Convert response to OpenAI format
            return self.convert_response(response)
            
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")
    
    def convert_response(self, response) -> Dict:
        """Convert Gemini response to OpenAI-compatible format"""
        try:
            # Get the response text
            if hasattr(response, 'text') and response.text:
                content = response.text
                function_call = None
            elif hasattr(response, 'parts') and response.parts:
                # Check for function calls
                part = response.parts[0]
                if hasattr(part, 'function_call') and part.function_call:
                    content = None
                    function_call = {
                        'name': part.function_call.name,
                        'arguments': json.dumps(dict(part.function_call.args))
                    }
                else:
                    content = part.text if hasattr(part, 'text') else str(part)
                    function_call = None
            else:
                content = "No response generated"
                function_call = None
            
            # Build message
            message = {}
            if content:
                message['content'] = content
            if function_call:
                message['function_call'] = function_call
            message['role'] = 'assistant'
            
            # Calculate token usage (approximate)
            prompt_tokens = 0
            completion_tokens = len(content.split()) if content else 0
            
            if hasattr(response, 'usage_metadata'):
                prompt_tokens = getattr(response.usage_metadata, 'prompt_token_count', prompt_tokens)
                completion_tokens = getattr(response.usage_metadata, 'candidates_token_count', completion_tokens)
            
            return {
                'choices': [{
                    'message': message,
                    'finish_reason': 'stop' if content else 'function_call'
                }],
                'usage': {
                    'prompt_tokens': prompt_tokens,
                    'completion_tokens': completion_tokens,
                    'total_tokens': prompt_tokens + completion_tokens
                }
            }
            
        except Exception as e:
            raise Exception(f"Response conversion error: {str(e)}")


# Global client instance
_gemini_client = None

def get_gemini_client():
    """Get or create Gemini client instance"""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = GeminiLLMClient()
    return _gemini_client

def gemini_chat_completion_create(**kwargs):
    """
    Main function for creating chat completions with Gemini
    Drop-in replacement for openai.ChatCompletion.create()
    Fixed array schema handling for ProAgent
    """
    client = get_gemini_client()
    return client.create_completion(**kwargs)
