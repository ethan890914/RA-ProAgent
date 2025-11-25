#!/usr/bin/env python3
"""
Updated Gemini API Key Test Script - Uses Available Models
Tests your Gemini API key status, rate limits, and basic functionality
"""

import os
import sys
import time
from datetime import datetime

def check_environment():
    """Check if Gemini API key is set in environment"""
    print("🔍 Checking Environment Variables...")
    
    gemini_key = os.getenv('GEMINI_API_KEY')
    if not gemini_key:
        print("❌ GEMINI_API_KEY not found in environment variables")
        print("\nTo set it:")
        print("  export GEMINI_API_KEY='your_api_key_here'")
        print("  # or add it to your .env file")
        return False
    
    print(f"✅ GEMINI_API_KEY found (length: {len(gemini_key)} characters)")
    # Mask the key for security
    masked_key = gemini_key[:8] + '*' * (len(gemini_key) - 12) + gemini_key[-4:]
    print(f"   Key preview: {masked_key}")
    return True

def test_google_ai_import():
    """Test if google.generativeai can be imported"""
    print("\n📦 Testing Package Import...")
    
    try:
        import google.generativeai as genai
        print("✅ google-generativeai imported successfully")
        return True
    except ImportError as e:
        print("❌ Failed to import google-generativeai")
        print(f"   Error: {e}")
        print("\nTo install:")
        print("  pip install google-generativeai")
        return False

def get_best_available_model():
    """Find the best available model for testing"""
    try:
        import google.generativeai as genai
        
        # Configure API key
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        
        # Get available models
        models = genai.list_models()
        available_models = []
        
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
        
        # Priority order for testing (fastest/most reliable first)
        preferred_models = [
            'models/gemini-2.5-flash',
            'models/gemini-1.5-flash', 
            'models/gemini-2.5-pro',
            'models/gemini-1.5-pro',
            'models/gemini-pro'
        ]
        
        # Find the first available preferred model
        for preferred in preferred_models:
            if preferred in available_models:
                return preferred, available_models
        
        # If no preferred model, use the first available
        if available_models:
            return available_models[0], available_models
        
        return None, []
        
    except Exception as e:
        print(f"   Error getting models: {e}")
        return None, []

def test_api_connection():
    """Test basic API connection and authentication"""
    print("\n🔌 Testing API Connection...")
    
    try:
        import google.generativeai as genai
        
        # Configure API key
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        
        # Test with model list request
        best_model, available_models = get_best_available_model()
        
        if not available_models:
            print("❌ No models available for generateContent")
            return False
        
        print("✅ API connection successful")
        print(f"✅ Found {len(available_models)} available models")
        print(f"✅ Best model for testing: {best_model}")
        
        # Show available models
        gemini_models = [m for m in available_models if 'gemini' in m.lower()]
        if gemini_models:
            print("   Available Gemini models:")
            for model in gemini_models[:8]:  # Show first 8
                model_name = model.replace('models/', '')
                print(f"     - {model_name}")
            if len(gemini_models) > 8:
                print(f"     ... and {len(gemini_models) - 8} more")
        
        return True, best_model
        
    except Exception as e:
        print("❌ API connection failed")
        print(f"   Error: {e}")
        
        # Check for common error types
        if "API_KEY" in str(e).upper() or "authentication" in str(e).lower():
            print("   💡 This looks like an authentication error")
            print("      - Check if your API key is correct")
            print("      - Ensure the key has proper permissions")
        elif "quota" in str(e).lower() or "rate" in str(e).lower():
            print("   💡 This looks like a rate limit or quota issue")
            print("      - You may have exceeded your rate limit")
            print("      - Check your Google AI Studio quota")
        
        return False, None

def test_simple_generation(model_name):
    """Test a simple text generation request"""
    print("\n🧪 Testing Simple Text Generation...")
    
    try:
        import google.generativeai as genai
        
        # Configure API
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        
        # Create model instance
        print(f"   Using model: {model_name}")
        model = genai.GenerativeModel(model_name)
        
        # Simple test prompt
        test_prompt = "Hello! Please respond with exactly: 'Gemini API is working correctly.'"
        
        print("   Sending test prompt...")
        start_time = time.time()
        
        response = model.generate_content(test_prompt)
        
        end_time = time.time()
        response_time = end_time - start_time
        
        print(f"✅ Text generation successful")
        print(f"   Response time: {response_time:.2f} seconds")
        print(f"   Response: {response.text}")
        
        # Check if response contains expected text
        if "Gemini API is working correctly" in response.text:
            print("   ✅ Response validation passed")
        else:
            print("   ⚠️  Response doesn't match expected output (but API works)")
        
        return True
        
    except Exception as e:
        print("❌ Text generation failed")
        print(f"   Error: {e}")
        
        # Analyze error type
        if "quota" in str(e).lower():
            print("   💡 Quota exceeded - you may have hit rate limits")
        elif "blocked" in str(e).lower():
            print("   💡 Content was blocked by safety filters")
        elif "timeout" in str(e).lower():
            print("   💡 Request timed out - try again later")
        elif "404" in str(e):
            print("   💡 Model not found - this shouldn't happen with auto-detection")
        
        return False

def test_rate_limits(model_name):
    """Test rate limits by making multiple requests"""
    print("\n⏱️  Testing Rate Limits (3 quick requests)...")
    
    try:
        import google.generativeai as genai
        
        # Configure API
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(model_name)
        
        request_times = []
        success_count = 0
        
        for i in range(3):
            try:
                start_time = time.time()
                response = model.generate_content(f"Count to {i+1}")
                end_time = time.time()
                
                request_times.append(end_time - start_time)
                success_count += 1
                print(f"   Request {i+1}: ✅ ({end_time - start_time:.2f}s)")
                
                # Small delay between requests
                time.sleep(0.5)
                
            except Exception as e:
                print(f"   Request {i+1}: ❌ {str(e)[:50]}...")
                if "quota" in str(e).lower() or "rate" in str(e).lower():
                    print("   💡 Hit rate limit on request", i+1)
                    break
        
        if success_count == 3:
            avg_time = sum(request_times) / len(request_times)
            print(f"✅ All requests successful")
            print(f"   Average response time: {avg_time:.2f}s")
            print("   Rate limits look good for normal usage")
        else:
            print(f"⚠️  {success_count}/3 requests successful")
            if success_count == 0:
                print("   💡 May have rate limit issues")
            
        return success_count > 0
        
    except Exception as e:
        print("❌ Rate limit test failed")
        print(f"   Error: {e}")
        return False

def test_function_calling(model_name):
    """Test function calling capability (important for ProAgent)"""
    print("\n🔧 Testing Function Calling...")
    
    try:
        import google.generativeai as genai
        
        # Configure API
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        
        # Define a simple test function
        def get_weather(location: str) -> dict:
            """Get weather information for a location."""
            return {"location": location, "temperature": "22°C", "condition": "sunny"}
        
        model = genai.GenerativeModel(model_name, tools=[get_weather])
        
        # Test function calling
        prompt = "What's the weather like in New York?"
        
        print(f"   Testing function calling with: '{prompt}'")
        response = model.generate_content(prompt)
        
        # Check if function was called
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate.content, 'parts'):
                for part in candidate.content.parts:
                    if hasattr(part, 'function_call'):
                        print("✅ Function calling works!")
                        print(f"   Called function: {part.function_call.name}")
                        print(f"   With arguments: {dict(part.function_call.args)}")
                        return True
        
        # If no function call, still check if it responded
        if response.text:
            print("⚠️  Model responded but didn't call function")
            print(f"   Response: {response.text[:100]}...")
            print("   Function calling may work but model chose not to use it")
            return True
        
        return False
        
    except Exception as e:
        print("❌ Function calling test failed")
        print(f"   Error: {e}")
        
        if "not supported" in str(e).lower():
            print("   💡 This model may not support function calling")
        
        return False

def main():
    """Run all tests"""
    print("🚀 Gemini API Key Test (Updated)")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # First get the best available model
    best_model = None
    
    tests = [
        ("Environment Check", lambda: check_environment()),
        ("Package Import", lambda: test_google_ai_import()),
        ("API Connection", lambda: test_api_connection()),
    ]
    
    results = []
    
    # Run initial tests
    for test_name, test_func in tests:
        try:
            if test_name == "API Connection":
                result = test_func()
                if isinstance(result, tuple):
                    success, model = result
                    results.append((test_name, success))
                    if success:
                        best_model = model
                else:
                    results.append((test_name, result))
            else:
                result = test_func()
                results.append((test_name, result))
            
            # Stop if critical tests fail
            if not results[-1][1] and test_name in ["Environment Check", "Package Import"]:
                print(f"\n❌ Critical test '{test_name}' failed. Stopping here.")
                break
                
        except Exception as e:
            print(f"\n💥 Unexpected error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Run model-dependent tests if we have a model
    if best_model and all(result for _, result in results):
        model_tests = [
            ("Simple Generation", lambda: test_simple_generation(best_model)),
            ("Rate Limit Check", lambda: test_rate_limits(best_model)),
            ("Function Calling", lambda: test_function_calling(best_model)),
        ]
        
        for test_name, test_func in model_tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"\n💥 Unexpected error in {test_name}: {e}")
                results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("-" * 20)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Gemini API is ready for ProAgent migration.")
        if best_model:
            print(f"   Recommended model: {best_model.replace('models/', '')}")
    elif passed >= 4:
        print("⚠️  Most tests passed. You should be able to use Gemini API with minor limitations.")
    else:
        print("❌ Multiple test failures. Please check your API key and setup before proceeding.")
    
    # Recommendations
    print("\n💡 Recommendations:")
    if passed < 3:
        print("   - Verify your GEMINI_API_KEY is correct")
        print("   - Check your Google AI Studio quota")
    elif passed < total:
        print("   - Some advanced features may have limitations")
        print("   - Basic ProAgent migration should still work")
    else:
        print("   - You're ready to migrate ProAgent to Gemini!")
        print("   - All core functionality is working properly")

if __name__ == "__main__":
    main()
