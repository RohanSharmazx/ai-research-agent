from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from graph import research_graph

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Request Model
class ResearchRequest(BaseModel):
    question: str


# Research API
@app.post("/research")
async def research(data: ResearchRequest):

    result = research_graph.invoke({

        "question": data.question,

        "search_query": "",

        "search_results": [],

        "report": "",

        "feedback": "",

        "needs_more_research": False,

        "iteration_count": 0

    })

    sources = []

    for source in result["search_results"]:

        sources.append({
            "title": source["title"],
            "url": source["url"]
        })

    return {

        "report": result["report"],

        "sources": sources

    }