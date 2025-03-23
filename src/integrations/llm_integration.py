import os
import requests
import json

def connect_to_ollama():
    url = "http://localhost:11434/api/generate"  # Ollama's default endpoint
    headers = {
        "Content-Type": "application/json"
    }

    return url, headers

def send_query_to_ollama(query, model="llama3"):
    url, headers = connect_to_ollama()
    payload = {
        "model": model,  # Use the specified model
        "prompt": query,
        "stream": False # Set to False to receive the full response at once
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, stream=False)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error communicating with Ollama: {response.status_code} - {response.text}")

def format_response(response):
    return response.get("response", response.get("content", "No response received."))

class LLMIntegration:
    def __init__(self):
        # No API key needed for local Ollama
        pass

    def is_related_to_apple(self, prompt, model="llama3"):
        classification_prompt = f"Is the following query related to Apple products or about an apple competitor? Answer with 'yes' or 'no'.\nQuery: {prompt}"
        try:
            response = send_query_to_ollama(classification_prompt, model)
            formatted_response = format_response(response)
            return "yes" in formatted_response.lower()
        except Exception as e:
            print(f"Error classifying topic: {e}")
            return False

    def generate_response(self, prompt, topic=None, model="llama3"):
        if not self.is_related_to_apple(prompt):
            return "I am an Apple product sales assistant and can only answer questions about Apple products."
        try:
            response = send_query_to_ollama(prompt, model)
            formatted_response = format_response(response)
            return formatted_response
        except Exception as e:
            return f"Error generating response: {e}"