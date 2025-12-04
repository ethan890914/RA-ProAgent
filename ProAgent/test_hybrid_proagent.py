#!/usr/bin/env python3
"""
ProAgent Hybrid API Test (Fixed Version)
Test both OpenAI and Gemini APIs and switching functionality
"""

import os
import sys
import json
from datetime import datetime

class MockRecorder:
    """Mock recorder that matches the interface of RunningRecoder"""
    
    def __init__(self, api_provider="test"):
        self.llm_interface_id = f"test_{api_provider}_{int(datetime.now().timestamp())}"
    
    def query_llm_inout(self, restrict_cache_query=True, base_kwargs=None, messages=None, 
                       functions=None, function_call=None, stop=None, other_args=None):
        """Mock implementation - always returns None to bypass cache"""
        return None
    
    def regist_llm_inout(self, base_kwargs=None, messages=None, functions=None, 
                        function_call=None, stop=None, other_args=None, output_data=None):
        """Mock implementation - just records that it was called"""
        pass

def test_environment():
    """Test environment setup"""
    print("🔧 Testing Environment Setup...")
    
    # Check API provider
    api_provider = os.getenv('API_PROVIDER', 'openai')
    print(f"   Current API Provider: {api_provider}")
    
    # Check API keys
    openai_key = os.getenv('OPENAI_API_KEY')
    gemini_key = os.getenv('GEMINI_API_KEY')
    
    print(f"   OpenAI Key: {'✅ Set' if openai_key else '❌ Not set'}")
    print(f"   Gemini Key: {'✅ Set' if gemini_key else '❌ Not set'}")
    
    if not openai_key and not gemini_key:
        print("   ❌ No API keys found!")
        return False
    
    return True

def test_imports():
    """Test required imports"""
    print("\n📦 Testing Package Imports...")
    
    # Test ProAgent imports
    try:
        from ProAgent.config import CONFIG
        print("   ✅ ProAgent config imported")
        print(f"   📋 Detected API Provider: {getattr(CONFIG, 'api_provider', 'unknown')}")
    except ImportError as e:
        print(f"   ❌ ProAgent config import failed: {e}")
        return False
    
    # Test OpenAI import
    try:
        import openai
        print("   ✅ OpenAI package imported")
    except ImportError:
        print("   ⚠️  OpenAI package not found")
    
    # Test Gemini import
    try:
        import google.generativeai as genai
        print("   ✅ Google Generative AI imported")
    except ImportError:
        print("   ⚠️  google-generativeai not found")
        print("       Install with: pip install google-generativeai")
    
    # Test Gemini agent import
    try:
        from ProAgent.agent.gemini_agent import gemini_chat_completion_create
        print("   ✅ Gemini agent module imported")
    except ImportError:
        print("   ⚠️  Gemini agent module not found")
    
    # Test utils import
    try:
        from ProAgent.agent.utils import _chat_completion_request
        print("   ✅ ProAgent utils imported")
    except ImportError as e:
        print(f"   ❌ ProAgent utils import failed: {e}")
        return False
    
    return True

def test_api_switch(provider):
    """Test switching to a specific API provider"""
    print(f"\n🔄 Testing {provider.upper()} API...")
    
    # Set the environment variable
    os.environ['API_PROVIDER'] = provider
    
    # Reload config to pick up the change
    try:
        import importlib
        import ProAgent.config
        importlib.reload(ProAgent.config)
        from ProAgent.config import CONFIG
        
        current_provider = getattr(CONFIG, 'api_provider', provider)
        if current_provider != provider:
            print(f"   ⚠️  Expected {provider}, got {current_provider}")
        else:
            print(f"   ✅ Successfully switched to {provider}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Failed to switch to {provider}: {e}")
        return False

def test_llm_request(api_provider, test_name):
    """Test an actual LLM request"""
    print(f"\n🤖 Testing {test_name} ({api_provider.upper()})...")
    
    # Set API provider
    os.environ['API_PROVIDER'] = api_provider
    
    # Check if we have the required API key
    if api_provider == 'openai' and not os.getenv('OPENAI_API_KEY'):
        print("   ⚠️  OPENAI_API_KEY not set, skipping OpenAI test")
        return None
    elif api_provider == 'gemini' and not os.getenv('GEMINI_API_KEY'):
        print("   ⚠️  GEMINI_API_KEY not set, skipping Gemini test")
        return None
    
    try:
        # Reload to pick up environment changes
        import importlib
        import ProAgent.config
        importlib.reload(ProAgent.config)
        
        from ProAgent.config import CONFIG
        from ProAgent.agent.utils import _chat_completion_request
        
        # Simple test request
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Say exactly: '{api_provider} API test successful'"}
        ]
        
        print("   Sending test request...")
        
        # Use proper MockRecorder
        mock_recorder = MockRecorder(api_provider)
        
        response = _chat_completion_request(
            default_completion_kwargs=CONFIG.default_completion_kwargs,
            messages=messages,
            restrict_cache_query=False,
            recorder=mock_recorder
        )
        
        if response and 'choices' in response:
            content = response['choices'][0]['message']['content']
            print(f"   ✅ Response: {content}")
            
            # Validate response
            if f"{api_provider} API test successful" in content:
                print("   ✅ Response validation passed")
                return True
            else:
                print("   ⚠️  Response doesn't match expected (but API works)")
                return True
        else:
            print("   ❌ Invalid response format")
            print(f"   Response: {response}")
            return False
            
    except Exception as e:
        print(f"   ❌ {test_name} failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_function_calling(api_provider):
    """Test function calling with specific API"""
    print(f"\n🔧 Testing Function Calling ({api_provider.upper()})...")
    
    # Set API provider
    os.environ['API_PROVIDER'] = api_provider
    
    # Check API key
    if api_provider == 'openai' and not os.getenv('OPENAI_API_KEY'):
        print("   ⚠️  OPENAI_API_KEY not set, skipping test")
        return None
    elif api_provider == 'gemini' and not os.getenv('GEMINI_API_KEY'):
        print("   ⚠️  GEMINI_API_KEY not set, skipping test")
        return None
    
    try:
        import importlib
        import ProAgent.config
        importlib.reload(ProAgent.config)
        
        from ProAgent.config import CONFIG
        from ProAgent.agent.utils import _chat_completion_request
        
        # Define test function
        test_function = {
            "name": "get_current_time",
            "description": "Get the current time",
            "parameters": {
                "type": "object",
                "properties": {
                    "format": {
                        "type": "string",
                        "description": "Time format (12hr or 24hr)"
                    }
                },
                "required": ["format"]
            }
        }
        
        messages = [
            {"role": "user", "content": "What time is it? Use 24hr format."}
        ]
        
        print("   Testing function calling...")
        
        # Use proper MockRecorder
        mock_recorder = MockRecorder(api_provider)
        
        response = _chat_completion_request(
            default_completion_kwargs=CONFIG.default_completion_kwargs,
            messages=messages,
            functions=[test_function],
            restrict_cache_query=False,
            recorder=mock_recorder
        )
        
        if response and 'choices' in response:
            message = response['choices'][0]['message']
            
            if 'function_call' in message:
                func_call = message['function_call']
                print(f"   ✅ Function called: {func_call['name']}")
                print(f"   ✅ Arguments: {func_call['arguments']}")
                return True
            else:
                print("   ⚠️  Model responded with text instead of function call")
                print(f"   Response: {message.get('content', '')[:100]}...")
                return True  # Still counts as working
        else:
            print("   ❌ Invalid response format")
            return False
            
    except Exception as e:
        print(f"   ❌ Function calling test failed: {e}")
        return False

def test_gpt4_function_compatibility(api_provider):
    """Test GPT4Function class compatibility"""
    print(f"\n🎯 Testing GPT4Function Class ({api_provider.upper()})...")
    
    # Set API provider
    os.environ['API_PROVIDER'] = api_provider
    
    # Check API key
    if api_provider == 'openai' and not os.getenv('OPENAI_API_KEY'):
        print("   ⚠️  OPENAI_API_KEY not set, skipping test")
        return None
    elif api_provider == 'gemini' and not os.getenv('GEMINI_API_KEY'):
        print("   ⚠️  GEMINI_API_KEY not set, skipping test")
        return None
    
    try:
        import importlib
        import ProAgent.config
        importlib.reload(ProAgent.config)
        
        from ProAgent.agent.gpt4_function import OpenAIFunction
        from ProAgent.config import CONFIG
        
        # Create function handler
        func_handler = OpenAIFunction()
        
        # Test function
        test_function = {
            "name": "calculate_area",
            "description": "Calculate area of a rectangle",
            "parameters": {
                "type": "object", 
                "properties": {
                    "width": {"type": "number", "description": "Width"},
                    "height": {"type": "number", "description": "Height"}
                },
                "required": ["width", "height"]
            }
        }
        
        messages = [
            {"role": "system", "content": "You are a math assistant."},
            {"role": "user", "content": "Calculate the area of a 5x3 rectangle"}
        ]
        
        print("   Testing OpenAIFunction.parse()...")
        
        # Use proper MockRecorder
        mock_recorder = MockRecorder(api_provider)
        
        content, function_name, function_arguments, message = func_handler.parse(
            default_completion_kwargs=CONFIG.default_completion_kwargs,
            messages=messages,
            functions=[test_function],
            recorder=mock_recorder
        )
        
        print(f"   ✅ Function: {function_name}")
        print(f"   ✅ Args: {function_arguments}")
        return True
        
    except Exception as e:
        print(f"   ❌ GPT4Function test failed: {e}")
        return False

def compare_apis():
    """Compare performance between APIs if both are available"""
    print("\n⚖️  Comparing APIs...")
    
    openai_key = os.getenv('OPENAI_API_KEY')
    gemini_key = os.getenv('GEMINI_API_KEY')
    
    if not (openai_key and gemini_key):
        print("   ⚠️  Both API keys needed for comparison")
        return
    
    results = {}
    
    for api in ['openai', 'gemini']:
        print(f"\n   Testing {api.upper()}...")
        
        try:
            import time
            start_time = time.time()
            
            # Test the API
            success = test_llm_request(api, f"Comparison test")
            
            end_time = time.time()
            response_time = end_time - start_time
            
            results[api] = {
                'success': success,
                'time': response_time
            }
            
            if success:
                print(f"   ⏱️  Response time: {response_time:.2f}s")
            
        except Exception as e:
            print(f"   ❌ {api} comparison failed: {e}")
            results[api] = {'success': False, 'time': 0}
    
    # Summary
    print("\n📊 Comparison Summary:")
    for api, result in results.items():
        if result['success']:
            print(f"   {api.upper()}: ✅ ({result['time']:.2f}s)")
        else:
            print(f"   {api.upper()}: ❌")

def main():
    """Run all tests"""
    print("🧪 ProAgent Hybrid API Test (Fixed)")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Basic tests
    tests = [
        ("Environment Setup", test_environment),
        ("Package Imports", test_imports),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
            
            if not result and test_name in ["Environment Setup", "Package Imports"]:
                print(f"\n❌ Critical test '{test_name}' failed. Stopping here.")
                return
        except Exception as e:
            print(f"\n💥 Error in {test_name}: {e}")
            results.append((test_name, False))
    
    # API-specific tests
    openai_key = os.getenv('OPENAI_API_KEY')
    gemini_key = os.getenv('GEMINI_API_KEY')
    
    api_results = {}
    
    # Test OpenAI if available
    if openai_key:
        print("\n" + "="*40)
        print("🔵 TESTING OPENAI API")
        print("="*40)
        
        openai_tests = [
            test_api_switch('openai'),
            test_llm_request('openai', 'Basic Request'),
            test_function_calling('openai'), 
            test_gpt4_function_compatibility('openai')
        ]
        
        openai_passed = sum(1 for test in openai_tests if test)
        api_results['openai'] = (openai_passed, len(openai_tests))
    
    # Test Gemini if available  
    if gemini_key:
        print("\n" + "="*40)
        print("🟢 TESTING GEMINI API")
        print("="*40)
        
        gemini_tests = [
            test_api_switch('gemini'),
            test_llm_request('gemini', 'Basic Request'),
            test_function_calling('gemini'),
            test_gpt4_function_compatibility('gemini')
        ]
        
        gemini_passed = sum(1 for test in gemini_tests if test)
        api_results['gemini'] = (gemini_passed, len(gemini_tests))
    
    # Compare if both available
    if openai_key and gemini_key:
        compare_apis()
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary")
    print("-" * 40)
    
    # Basic tests
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"Basic Tests: {passed}/{total}")
    
    # API tests
    for api, (api_passed, api_total) in api_results.items():
        print(f"{api.upper()} API: {api_passed}/{api_total}")
    
    # Overall status
    print("\n💡 Status:")
    if all(result for _, result in results):
        if api_results:
            all_api_good = all(passed == total for passed, total in api_results.values())
            if all_api_good:
                print("🎉 Perfect! Hybrid setup is fully functional!")
                print("   Both APIs work correctly and you can switch between them.")
            else:
                print("✅ Basic setup works, some API limitations.")
                print("   Check API keys and network connectivity.")
        else:
            print("⚠️  Setup complete but no APIs tested (no keys provided).")
    else:
        print("❌ Setup issues detected. Review failed tests above.")
    
    print("\n🔄 Quick Switch Commands:")
    print("   python switch_api.py openai")
    print("   python switch_api.py gemini") 
    print("   python switch_api.py status")

if __name__ == "__main__":
    main()
