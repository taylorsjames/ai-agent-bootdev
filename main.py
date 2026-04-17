import os
from dotenv import load_dotenv
from google import genai



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if api_key == None:
    raise RuntimeError("Unable to load gemini API key, please ensure key is valid and not expired and is saved in environment variable")

def main():
    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=user_prompt
)
    if response.usage_metadata == None:
        raise RuntimeError("Response empty, please check API key or connection")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count

    print(f'User Prompt: {user_prompt}')
    print(f'Prompt tokens: {prompt_token_count}')
    print(f'Response tokens: {response_token_count}')
    print(f'Response:\n{response.text}')


if __name__ == "__main__":
    main()
