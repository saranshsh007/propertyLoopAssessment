from langchain.prompts import PromptTemplate
from utils.config import CustomAzureChatOpenAI
from prompts.prompts import tenancy_faq_prompt

tenancy_faq_prompt = PromptTemplate(
    input_variables=["user_text", "location"],
    template= tenancy_faq_prompt
)

def handle_tenancy_faq(user_text, location=""):
    prompt = tenancy_faq_prompt.format(user_text=user_text, location=location)
    
    llm = CustomAzureChatOpenAI(temperature=0.3, max_tokens=1000)
    messages = [
        {"role": "system", "content": "You are a tenancy law assistant."},
        {"role": "user", "content": prompt}
    ]
    
    response = llm.invoke(messages)
    return response.content.strip()
