from propertyLoopAssessment.src.router_graph import build_router_graph

def run_router_flow(image_path="", user_text="", location=""):
    graph = build_router_graph()
    # Initialize state
    # Ensure image_path, user_text, and location are strings
    state = {
        "image_path": image_path or "",
        "user_text": user_text or "",
        "location": location or "",
        "route": "agent2",  # Default fallback to agent2
        "final_result": ""
    }

    result = graph.invoke(state)

    # Debug info
    print("\n=== Router Decision ===")
    print(f"Route Taken: {result.get('route', 'Unknown')}")
    print("\n=== Final Response ===")
    print(result["final_result"])

    return result["final_result"]
