from app.config import get_llm

# Convert user query → multiple search queries

def planner_agent(state):

    llm = get_llm()

    query = state["query"]

    prompt = f"""
    Break the following research question into 5 web search queries.

    Question:
    {query}

    Return only the queries, one per line.
    """

    response = llm.invoke(prompt)

    queries = response.content.split("\n")

    queries = [q.strip() for q in queries if q.strip() != ""]

    state["search_queries"] = queries

    return state