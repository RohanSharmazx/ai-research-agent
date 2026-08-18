from nodes.planner import planner_node
from nodes.search import search_node
from nodes.writer import writer_node
from nodes.evaluator import should_continue,evaluator_node
from langgraph.graph import StateGraph,END
from state import AgentState

graph= StateGraph(AgentState)
graph.add_node("planner", planner_node)
graph.add_node("search", search_node)
graph.add_node("writer", writer_node )
graph.add_node("evaluator", evaluator_node)

graph.set_entry_point("planner")
graph.add_edge("planner", "search")
graph.add_edge("search", "writer")
graph.add_edge("writer", "evaluator")
graph.add_conditional_edges(
    "evaluator",
    should_continue,{ 
        "continue": "planner",
        "end": END 
    }
)

research_graph  = graph.compile()
