import os
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv

class CustomAzureChatOpenAI(AzureChatOpenAI):
    def __init__(self, temperature: float, max_tokens: int):
        load_dotenv()

        super().__init__(
            default_headers={"User-Id": os.getenv("USER_ID")},
            temperature=temperature,
            deployment_name=os.getenv('DEPLOYMENT_NAME'),
            model=os.getenv('MODEL_NAME'),
            max_tokens=max_tokens,
            openai_api_key=os.getenv('OPENAI_API_KEY',),
            request_timeout = 600
            
        )

# Usage example
if __name__ == "__main__":
    llm = CustomAzureChatOpenAI(temperature=0.0,max_tokens = 1000)
    response = llm.invoke('Where is Silicon City located?')
    print("Response: ", response.content)