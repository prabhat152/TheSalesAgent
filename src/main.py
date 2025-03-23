import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.steve import Steve
from agent.conversation import Conversation
from src.integrations.llm_integration import LLMIntegration

def main():
    print("Welcome to TheSalesMan! I'm Steve, your Apple product sales assistant.")
    
    # Initialize the conversation agent
    llm_integration = LLMIntegration()
    steve = Steve(llm_integration=llm_integration)
    conversation = Conversation(steve)

    # Print the initial conversation message
    print(f"Steve: {conversation.start_conversation()}")

    # Start the conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit","bye", "quit"]:
            print("Steve: Thank you for chatting! Have a great day!")
            break

        # Set the topic of the conversation based on the user input
        if any(keyword in user_input.lower() for keyword in ["apple", "iphone", "macbook", "ipad", "airpods", "mac mini", "apple watch"]):
            conversation.set_topic("apple_products")

        response = conversation.handle_user_input(user_input)  # Ensure correct method name
        print(f"Steve: {response}")

    # Example usage
    llm = LLMIntegration()
    prompt = "Tell me about the latest Apple products."
    response = llm.generate_response(prompt)
    print(response)

if __name__ == "__main__":
    main()