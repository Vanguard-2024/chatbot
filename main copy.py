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

# Chatbot function
def chatbot():
    # Display welcome message with date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("="*50)
    print(f"🗓️  Real Estate Assistant - {current_time}")
    print("="*50)
    print("Hello! I specialize in real estate. Type 'quit' to exit.")
    print("="*50)

    while True:
        # Get user input
        user_input = input("\033[94mYou: \033[0m")  # Blue text for user input
        if user_input.lower() == "quit":
            print("\033[92mGoodbye! Have a great day! 👋\033[0m")  # Green text for goodbye message
            break

        # Prepare messages for the chat model
        messages = [
            SystemMessage(content="You are a helpful assistant specializing in real estate. Provide insights on market trends, property advice, and local real estate news."),
            HumanMessage(content=user_input),
        ]

        # Get response from the model using `invoke()`
        try:
            response = chat_model.invoke(messages)
            print(f"\033[93mBot: {response.content}\033[0m")  # Yellow text for bot response
        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")  # Red text for errors

if __name__ == "__main__":
    chatbot()
