import os
import openai
from dotenv import load_dotenv

# Load the environment variables from dev.env
load_dotenv("dev.env")
# Set up your API key
openai.api_key = os.getenv("API_KEY")

# If you belong to multiple organizations and want to specify one:
# openai.organization = "YOUR_ORG_ID"

# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Give me a two sentence summary on the meaning of life"
    }]
)

# Extracting the response content
assistant_message = response['choices'][0]['message']['content']
print(assistant_message)