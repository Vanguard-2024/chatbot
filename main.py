import os
import datetime
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI configuration to use OpenRouter
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# Initialize ChatOpenAI with OpenRouter backend
chat_model = ChatOpenAI(model="meta-llama/llama-3.2-11b-vision-instruct:free", temperature=0.5)

# Helper to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper to display the header
def display_header():
    clear_screen()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 50)
    print(f"           Real Estate Assistant - {current_time}           ")
    print("=" * 50)
    print("Hello! I specialize in real estate. Type 'quit' to exit or 'clear' to reset the conversation.")
    print("=" * 50 + "\n")

# Chatbot function
def chatbot():
    chat_history = []  # Store the chat history
    display_header()

    # Opening message from the assistant
    assistant_intro = "Hi there! I'm your Real Estate Assistant. I can help with market trends, property advice, investment opportunities, and more. How can I assist you today?"
    chat_history.append({"role": "assistant", "content": assistant_intro, "timestamp": datetime.datetime.now().strftime("%H:%M:%S")})
    print(f"\033[92m[Assistant] {chat_history[-1]['timestamp']}\033[0m")  # Green for assistant
    print(f"{assistant_intro}\n")

    while True:
        # Get user input
        user_input = input("\033[94mYou: \033[0m")  # Blue for user input
        if user_input.lower() == "quit":
            print("\033[92mGoodbye! Have a great day! 👋\033[0m")  # Green for goodbye
            break
        if user_input.lower() == "clear":
            chat_history = []
            display_header()
            continue

        # Add user message to history
        chat_history.append({"role": "user", "content": user_input, "timestamp": datetime.datetime.now().strftime("%H:%M:%S")})

        # Prepare messages for the chat model
        messages = [
            SystemMessage(content="You are a helpful assistant specializing in real estate. Provide insights on market trends, property advice, and local real estate news."),
            HumanMessage(content=user_input),
        ]

        # Get response from the model using `invoke()`
        try:
            response = chat_model.invoke(messages)
            chat_history.append({"role": "assistant", "content": response.content, "timestamp": datetime.datetime.now().strftime("%H:%M:%S")})
            
            # Display updated chat history
            display_header()
            for message in chat_history:
                role = message['role']
                content = message['content']
                timestamp = message['timestamp']
                if role == 'user':
                    print(f"\033[94m[You] {timestamp}\033[0m")  # Blue for user
                    print(f"{content}\n")
                else:
                    print(f"\033[92m[Assistant] {timestamp}\033[0m")  # Green for assistant
                    print(f"{content}\n")

        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")  # Red for errors

if __name__ == "__main__":
    chatbot()
