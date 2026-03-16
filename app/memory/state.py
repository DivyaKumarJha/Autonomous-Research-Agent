from typing import TypedDict, List

class ResearchState(TypedDict):

    query: str

    search_queries: List[str]

    sources: List[str]

    documents: List[str]

    analysis: str

    report: str
    
# here i am defining the LangGraph state object. LangGraph will pass this between agents
# typedict is basically will allow every agent to know what each of the state object will look like and what keys it will have.