# Retrieve relevant documents from vector database and analyze them.
from app.config import get_llm
from app.tools.vector_store import search_documents


def analysis_agent(state):

    llm = get_llm()

    query = state["query"]

    docs = search_documents(query)

    context = ""

    for d in docs:
        context += d.page_content + "\n\n"

    prompt = f"""
    You are a research analyst.
    Answer the research question ONLY using the information
    from the documents below.

    Based on the following documents, extract the most important insights.

    Research Question:
    {query}

    Documents:
    {context}
    Tasks:

    1. Extract the key insights from the documents.
    2. Identify important concepts related to the research question.
    3. Summarize the findings clearly.

    Provide clear bullet point insights.
    """

    response = llm.invoke(prompt)

    state["analysis"] = response.content

    return state