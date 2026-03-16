from app.config import get_llm


def writer_agent(state):

    llm = get_llm()

    query = state["query"]
    analysis = state["analysis"]
    sources = state["sources"]

    sources_text = "\n".join(sources[:10])

    prompt = f"""
    You are a research assistant.
    Write a structured research report.

    Question:
    {query}

    Insights:
    {analysis}

    Sources:
    {sources_text}

    Format:

    Title
    Overview
    Key Findings
    Technical Analysis
    Conclusion
    References
    """

    response = llm.invoke(prompt)

    state["report"] = response.content

    return state