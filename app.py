import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

def main():
    # Configuration
    endpoint = "https://models.github.ai/inference"
    model = "gpt-4o-mini"
    token = os.environ["GITHUB_TOKEN"]

    # Initialize client
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    # Initialize conversation history with system message
    conversation_history = [
        SystemMessage("You are a helpful assistant.")
    ]

    print("=" * 60)
    print("Interactive Chatbot - Powered by DeepSeek-V3")
    print("=" * 60)
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    print("=" * 60)
    print()

    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
            print("\nGoodbye! Have a great day! 👋")
            break

        # Skip empty inputs
        if not user_input:
            continue

        # Add user message to conversation history
        conversation_history.append(UserMessage(user_input))

        try:
            # Get response from the model
            response = client.complete(
                messages=conversation_history,
                temperature=1.0,
                top_p=1.0,
                max_tokens=1000,
                model=model
            )

            # Extract assistant's response
            assistant_response = response.choices[0].message.content

            # Add assistant's response to conversation history
            conversation_history.append(AssistantMessage(assistant_response))

            # Display the response
            print(f"\nAssistant: {assistant_response}\n")

        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            # Remove the last user message if there was an error
            conversation_history.pop()

if __name__ == "__main__":
    main()

