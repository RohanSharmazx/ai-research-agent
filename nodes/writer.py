from langchain_core.messages import HumanMessage,SystemMessage
from config import llm
from utils.prompts import WRITER_SYSTEM_PROMPT_V1
from utils.formatter import format_search_result
from state import AgentState


def writer_node(state: AgentState) -> AgentState:
    """This is the writer node it writes the results of the user's query and returns the report."""
    user_query= state["question"]
    formatted_context = format_search_result(state["search_results"])
    human_message = f"""
    Question:
    {user_query}

    Search Results:
    {formatted_context}"""
    system_prompt= SystemMessage(WRITER_SYSTEM_PROMPT_V1)
    final_message= [system_prompt, HumanMessage(human_message)]
    response = llm.invoke(final_message)
    return {"report": response.content}
