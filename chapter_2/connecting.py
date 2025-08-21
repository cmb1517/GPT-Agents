"""
Within the request, the messages block describes a set of messages and roles used in a
request. Messages for a chat completions model can be defined in three roles:
    - System role—A message that describes the request’s rules and guidelines. It can
      often be used to describe the role of the LLM in making the request.
    - User role—Represents and contains the message from the user.
    - Assistant role—Can be used to capture the message history of previous responses
      from the LLM. It can also inject a message history when perhaps none existed.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)


# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",  # gpt-4 turbo or a model of your preference
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
        )       
    return response.choices[0].message.content


# Example usage
user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)
