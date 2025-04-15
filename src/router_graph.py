from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal
from agents.agent1_issue_detection import analyze_property_issue
from agents.agent2_tenancy_faq import handle_tenancy_faq
from agents.agent_router import decide_agent

AgentRoute = Literal["agent1", "agent2", "clarify"]


class RouterState(TypedDict):
    image_path: str
    user_text: str
    location: str
    route: AgentRoute
    final_result: str

def route_node(state: RouterState) -> RouterState:
    route = decide_agent(state.get("image_path", ""), state.get("user_text", ""))
    state["route"] = route
    return state

def clarify_node(state: RouterState) -> RouterState:
   
    state["final_result"] = (
        "🤔 I'm not sure whether this is a property issue or a tenancy question. "
        "Could you clarify if this is about a specific property problem (like leaks or damages) "
        "or a legal/tenancy question?"
    )
    return state



# Agent 1: Property Issue Detection
def issue_node(state: RouterState) -> RouterState:
    image_path = state["image_path"]
    user_text = state.get("user_text", "")
    result = analyze_property_issue(image_path, user_text)
    state["final_result"] = result
    return state

# Agent 2: Tenancy FAQ
def faq_node(state: RouterState) -> RouterState:
    user_text = state["user_text"]
    location = state.get("location", "")
    result = handle_tenancy_faq(user_text, location)
    state["final_result"] = result
    return state

def build_router_graph():
    graph = StateGraph(RouterState)

    graph.add_node("routing_logic", route_node)
    graph.add_node("agent1", issue_node)
    graph.add_node("agent2", faq_node)
    graph.add_node("clarify", clarify_node)

    # Route based on result of route_node
    graph.add_conditional_edges("routing_logic", lambda s: s["route"], {
        "agent1": "agent1",
        "agent2": "agent2",
        "clarify": "clarify", 
    })

    # Endpoints
    graph.set_finish_point("agent1")
    graph.set_finish_point("agent2")
    graph.set_finish_point("clarify")

    graph.set_entry_point("routing_logic")
    return graph.compile()
