from duckduckgo_search import DDGS

def search_web(query, max_results=5):

    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)

        for r in results:
            urls.append(r["href"])

    return urls