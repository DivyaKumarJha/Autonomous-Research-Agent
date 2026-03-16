from app.tools.web_search import search_web

# this runs web searches and collect URLs.

def research_agent(state):

    queries = state["search_queries"]

    urls = []

    for q in queries:

        results = search_web(q)

        urls.extend(results)

    urls = list(set(urls))

    state["sources"] = urls

    return state