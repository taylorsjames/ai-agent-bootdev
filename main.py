import os
from dotenv import load_dotenv
from google import genai
import argparse

#loading stuff we need

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#check if api key loaded properly
if api_key == None:
    raise RuntimeError("Unable to load gemini API key, please ensure key is valid and not expired and is saved in environment variable")

#prompt user for input
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


def main():
    
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=args.user_prompt
)
    if response.usage_metadata == None:
        raise RuntimeError("Response empty, please check API key or connection")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count

    print(f'User Prompt: {args.user_prompt}')
    print(f'Prompt tokens: {prompt_token_count}')
    print(f'Response tokens: {response_token_count}')
    print(f'Response:\n{response.text}')


if __name__ == "__main__":
    main()
