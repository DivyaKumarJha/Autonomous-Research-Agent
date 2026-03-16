from fastapi import FastAPI
from app.graph.research_graph import run_research

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Autonomous Research Agent API"}

@app.post("/research")

def research(query: str):

    result = run_research(query)

    return result