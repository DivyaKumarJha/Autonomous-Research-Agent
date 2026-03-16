from pydantic import BaseModel
from typing import List

class ResearchReport(BaseModel):

    title: str

    overview: str

    key_findings: List[str]

    technical_analysis: str

    conclusion: str

    references: List[str]