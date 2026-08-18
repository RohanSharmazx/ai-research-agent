from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

tavily_client= TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

MAX_ITERATIONS = 3