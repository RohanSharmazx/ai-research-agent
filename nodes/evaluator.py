from state import AgentState,Evaluator
from langchain_core.messages import SystemMessage,HumanMessage
from langgraph.graph import END
from utils.prompts import EVALUATOR_SYSTEM_PROMPT
from config import llm,MAX_ITERATIONS



def evaluator_node(state: AgentState) -> AgentState:
    """This node decides whether the user question has been answered clearly or something missing."""
    query = state["question"]
    report = state["report"]
    report_of_query = f"""
    Question:
    {query}
    Report:
    {report}"""

    system_message = SystemMessage(EVALUATOR_SYSTEM_PROMPT)
    total_messages = [system_message,HumanMessage(report_of_query)]
    structured_llm = llm.with_structured_output(Evaluator)
    response = structured_llm.invoke(total_messages)
    return {"feedback": response.feedback, "needs_more_research":response.needs_more_research}
    

def should_continue(state: AgentState):
    """Decide whether to continue researching or finish."""

    if (
        state["needs_more_research"]
        and state["iteration_count"] < MAX_ITERATIONS
    ):
        return "continue"

    return "end"