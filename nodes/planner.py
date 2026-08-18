from state import AgentState
from langchain_core.messages import SystemMessage,HumanMessage
from config import llm
from utils.prompts import PLANNER_PROMPT

def planner_node(state: AgentState) -> AgentState:
    """This node converts the user question into a query to search"""
    user_question= state["question"]
   
    messages=[SystemMessage(content=PLANNER_PROMPT),HumanMessage(content=user_question)]
    response = llm.invoke(messages)
    return {
    "search_query": response.content,
    "iteration_count": state["iteration_count"] + 1
}

