from typing import TypedDict,Annotated,Sequence,List
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel

class SearchResult(TypedDict):
    title: str
    url: str
    content: str
    score: float

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage] , add_messages]
    question: str
    search_query: str
    search_results: List[SearchResult]
    report: str
    iteration_count: int
    sources: List[str]
    needs_more_research: bool
    feedback: str
    

class Evaluator(BaseModel):
    needs_more_research: bool
    feedback: str

