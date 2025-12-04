from openai import OpenAI, RateLimitError, APIError
import json

client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": "hello"}]
    )
    print("Success:", response)

except RateLimitError as e:
    print("\n=== RateLimitError Caught ===")

    # Print JSON body (important!)
    try:
        print("\nError JSON body:")
        print(json.dumps(e.response.json(), indent=2))
    except Exception:
        print("No JSON body available")

    # Print headers
    print("\nHeaders:")
    for k, v in e.response.headers.items():
        print(f"{k} : {v}")

except APIError as e:
    # Catch other API errors to help debugging
    print("\n=== APIError Caught ===")
    try:
        print(json.dumps(e.response.json(), indent=2))
    except Exception:
        print(e)

except Exception as e:
    print("\n=== Other Exception ===")
    print(e)
