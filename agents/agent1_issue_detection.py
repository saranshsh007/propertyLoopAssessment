import base64
from langchain.prompts import PromptTemplate
from utils.config import CustomAzureChatOpenAI
from prompts.prompts import issue_detection_prompt

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def analyze_property_issue(image_path="", user_text=None):
    llm = CustomAzureChatOpenAI(temperature=0.3, max_tokens=1000)

    # If image is provided, include image context and attachment
    if image_path:
        base64_image = image_to_base64(image_path)
        prompt_text = issue_detection_prompt.format(
            image_context="See attached image below.",
            user_text=user_text
        )

        messages = [
            {"role": "system", "content": "You are an AI assistant for property issue detection."},
            {"role": "user", "content": [
                {"type": "text", "text": prompt_text},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]}
        ]
    else:
        prompt_text = issue_detection_prompt.format(
            image_context="No image provided.",
            user_text=user_text
        )

        messages = [
            {"role": "system", "content": "You are an AI assistant for property issue detection."},
            {"role": "user", "content": prompt_text}
        ]

    # Call the model
    resp = llm.invoke(messages)
    result = resp.content.strip()
    return result
