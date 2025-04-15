from utils.config import CustomAzureChatOpenAI
from prompts.prompts import router_prompt

def decide_agent(image_path: str, user_text: str):
    llm = CustomAzureChatOpenAI(temperature=0.2, max_tokens=500)
    prompt = router_prompt.format(
        image_path=image_path,
        user_text=user_text
    )

    messages = [
        {"role": "system", "content": "You are a router that returns only 'agent1', 'agent2', or 'clarify'."},
        {"role": "user", "content": prompt}
    ]
    response = llm.invoke(messages)
    decision = response.content.strip().lower()

    # Logic for deciding whether to route to agent1, agent2, or ask for clarification
    if "agent1" in decision:
        return "agent1"
    elif "agent2" in decision:
        return "agent2"
    else:
        # If response is unclear, route to the clarification step
        return "clarify"
