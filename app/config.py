import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama


def get_llm():

    llm = ChatOllama(
        model="llama3.1",
        temperature=0.2
    )

    return llm