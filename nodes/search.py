from tools.search import web_search
from state import AgentState


def search_node(state:AgentState) -> AgentState:
    """This node invokes the web search tool and stores it results."""
    query = state["search_query"]
    results = web_search.invoke(query)
    return {"search_results": results}
