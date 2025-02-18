#!/usr/bin/env python3

import os
import requests
import argparse

# Load API key from environment variable
API_KEY = os.getenv("PERPLEXITY_API_KEY")

if not API_KEY:
    raise ValueError("Environment variable PERPLEXITY_API_KEY is not set.")

# List of available models (example models, update based on Perplexity's offerings)
AVAILABLE_MODELS = ["sonar-pro", "mistral-7b-instruct", "gpt-4", "gpt-3.5"]

# Function to query Perplexity AI API
def query_perplexity(model: str, max_tokens: int, user_query: str):
    """
    Make a call to the Perplexity AI API.

    Parameters:
        model (str): The model to use (e.g., "sonar-pro").
        max_tokens (int): Maximum number of tokens for the response.
        user_query (str): The user's query.

    Returns:
        dict: The API response as a dictionary.
    """
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": user_query},
        ],
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

    return response.json()

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Query Perplexity AI API.")
    
    # Argument to list available models
    parser.add_argument(
        "-l", "--list-models",
        action="store_true",
        help="List available models and exit."
    )
    
    # Argument to specify a model
    parser.add_argument(
        "-m", "--model",
        type=str,
        default="sonar-pro",
        help=f"Specify the model to use. Default is 'sonar-pro'. Available models: {', '.join(AVAILABLE_MODELS)}"
    )
    
    # Argument to specify max tokens
    parser.add_argument(
        "-t", "--max-tokens",
        type=int,
        default=1024,
        help="Specify the maximum number of tokens for the response. Default is 1024."
    )
    
    # Argument for the user query
    parser.add_argument(
        "-q", "--query",
        type=str,
        required=False,
        help="The query string to send to the API."
    )
    
    args = parser.parse_args()
    
    # Handle listing models
    if args.list_models:
        print("Available models:")
        for model in AVAILABLE_MODELS:
            print(f"- {model}")
        return
    
    # Validate selected model
    if args.model not in AVAILABLE_MODELS:
        print(f"Error: '{args.model}' is not a valid model.")
        print(f"Available models: {', '.join(AVAILABLE_MODELS)}")
        return
    
    # Ensure a query is provided if not listing models
    if not args.query:
        print("Error: You must provide a query using the '-q' or '--query' option.")
        return
    
    # Make the API call
    try:
        result = query_perplexity(args.model, args.max_tokens, args.query)
        print("Response:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

