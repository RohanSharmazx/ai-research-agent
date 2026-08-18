from config import tavily_client
from langchain.tools import tool
from state import SearchResult
from typing import List

@tool
def web_search(query: str):
    "Search the web for recent and relevant information using Tavily. Returns structured search results including titles, URLs, content, and relevance scores."
    try:
        response= tavily_client.search(query=query)
        content=[]
        for result in response.get("results",[]):
            title=result.get("title")
            url=result.get("url")
            details=result.get("content")
            score=result.get("score")
            content.append(SearchResult({"title":title,"url":url,"content":details,"score":score}))
        return content
    except Exception as e:
        return []