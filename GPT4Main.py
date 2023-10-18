import os
import openai
from dotenv import load_dotenv

# Load the environment variables from dev.env
load_dotenv("dev.env")
conversation_history = []
while(True):

    # Set up your API key
    openai.api_key = os.getenv("API_KEY")

    query = input("Send message for AI response: ")
    # Add the assistant's reply to the conversation history
    conversation_history.append({
        "role": "user",
        "content": f"{query}"
    })
    # Make the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    print(conversation_history)
    print(response)


    # Extracting the response content
    assistant_message = response['choices'][0]['message']['content']

    # Add the assistant's reply to the conversation history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    print(assistant_message)
    