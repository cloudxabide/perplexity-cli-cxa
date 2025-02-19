import os
import argparse
import requests

# Define the API endpoint and headers
API_URL = "https://api.perplexity.ai/chat/completions"
API_KEY = os.getenv("PERPLEXITY_API_TOKEN")

if not API_KEY:
    raise EnvironmentError("Environment variable PERPLEXITY_API_TOKEN is not set.")

# Function to list available models (example list, replace with actual API call if available)
def list_models():
    models = [
        "sonar-pro",
        "mistral-7b-instruct",
        "llama-2-70b-chat",
        "codellama-34b-instruct",
    ]
    print("Available Models:")
    for model in models:
        print(f"- {model}")

# Function to make an API call
def make_api_call(model, max_tokens):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": "Provide an example query response."},
        ],
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"API call failed: {response.status_code} - {response.text}")

    return response.json()

# Main function
def main():
    parser = argparse.ArgumentParser(description="Interact with the Perplexity AI API.")
    
    parser.add_argument("-t", "--tokens", type=int, default=100, help="Maximum number of tokens.")
    parser.add_argument("-m", "--model", type=str, default="sonar-pro", help="Model to use.")
    parser.add_argument("-l", "--list-models", action="store_true", help="List available models.")
    parser.add_argument("-h", "--help", action="store_true", help="Display this help message.")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return

    if args.list_models:
        list_models()
        return

    # Make the API call
    try:
        result = make_api_call(args.model, args.tokens)
        
        # Extract and print different parts of the result
        print("\n=== API Response ===")
        print(f"Model: {result.get('model', 'N/A')}")
        
        if 'choices' in result and len(result['choices']) > 0:
            choice = result['choices'][0]
            print("\n=== Message ===")
            print(choice.get("message", {}).get("content", "No content available."))
            
            print("\n=== Other Details ===")
            print(f"Finish Reason: {choice.get('finish_reason', 'N/A')}")
            
            print("\n=== Usage ===")
            usage = result.get("usage", {})
            for key, value in usage.items():
                print(f"{key.capitalize()}: {value}")
                
        else:
            print("No valid response found.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

