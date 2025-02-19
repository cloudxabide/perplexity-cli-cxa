#!/usr/bin/env python3

import os
import argparse
import requests

# Retrieve API key from environment variable
API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise EnvironmentError("PERPLEXITY_API_KEY environment variable not set.")

# Base URL for the Perplexity AI API
BASE_URL = "https://api.perplexity.ai/chat/completions"

max_tokens = "4000"

# List of available models (can be expanded based on API documentation)
# https://docs.perplexity.ai/guides/model-cards
AVAILABLE_MODELS = ["sonar-reasoning-pro", "sonar-reasoning", "sonar-pro", "sonar", "llama-3.1-sonar-small-128k-online", "llama-3.1-sonar-large-128k-online", "llama-3.1-sonar-huge-128k-online"]

def list_models():
    print("\nNote: the list of models is not dynamically retrieved from Perplexity.AI\n")
    print("Available models:")
    for model in AVAILABLE_MODELS:
        print(f"- {model}")

def call_api(model, max_tokens, query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": query}
        ],
        "max_tokens": max_tokens
    }

    response = requests.post(BASE_URL, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
    
    return response.json()

def parse_response(response):
    # Extract key parts of the response
    model_used = response.get("model", "N/A")
    choices = response.get("choices", [])
    usage = response.get("usage", {})

    # Print results with headers
    print("\n--- Model Used ---")
    print(model_used)

    print("\n--- Choices ---")
    for choice in choices:
        print(f"Message: {choice.get('message', {}).get('content', 'N/A')}")

    print("\n--- Usage ---")
    for key, value in usage.items():
        print(f"{key}: {value}")

def main():
    parser = argparse.ArgumentParser(description="Interact with Perplexity AI API.")
    
    parser.add_argument("-t", "--tokens", type=int, default=4000, help="Maximum number of tokens.")
    parser.add_argument("-m", "--model", type=str, default="sonar-pro", help="Model to use.")
    parser.add_argument("-l", "--list-models", action="store_true", help="List available models.")
    parser.add_argument("-q", "--query", type=str, required=False, help="Query to send to the API.")
    
    args = parser.parse_args()

    if args.list_models:
        list_models()
        return

    if not args.query:
        raise ValueError("A query must be provided unless listing models (-l).")

    if args.model not in AVAILABLE_MODELS:
        raise ValueError(f"Invalid model '{args.model}'. Use -l to list available models.")

    response = call_api(args.model, args.tokens, args.query)
    parse_response(response)

if __name__ == "__main__":
    main()

