from langgraph.graph import StateGraph, END

from app.memory.state import ResearchState
from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent
from app.agents.analysis_agent import analysis_agent
from app.agents.writer_agent import writer_agent

from app.tools.web_scrapper import scrape_article
from app.tools.vector_store import store_documents


def scrape_and_store(state):

    docs = []

    for url in state["sources"][:10]:

        text = scrape_article(url)

        if text != "":
            docs.append({
                "url": url,
                "text": text
            })

    state["documents"] = docs

    if len(docs) > 0:
        store_documents(docs)

    return state


def decision_node(state):

    analysis = state["analysis"]

    if "not enough information" in analysis.lower():

        return "research"

    return "writer"


builder = StateGraph(ResearchState)


builder.add_node("planner", planner_agent)

builder.add_node("research", research_agent)

builder.add_node("scrape_store", scrape_and_store)

builder.add_node("analysis", analysis_agent)

builder.add_node("writer", writer_agent)


builder.set_entry_point("planner")


builder.add_edge("planner", "research")

builder.add_edge("research", "scrape_store")

builder.add_edge("scrape_store", "analysis")

builder.add_conditional_edges(
    "analysis",
    decision_node,
    {
        "research": "research",
        "writer": "writer"
    }
)

builder.add_edge("writer", END)


graph = builder.compile()


def run_research(query):

    state = {
        "query": query,
        "search_queries": [],
        "sources": [],
        "documents": [],
        "analysis": "",
        "report": ""
    }
    for step in graph.stream(state):
        print(step)

    result = graph.invoke(state)

    return {
        "query": query,
        "report": result["report"]
    }