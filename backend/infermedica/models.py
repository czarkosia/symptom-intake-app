from typing import List, Optional, Dict
from pydantic import BaseModel, Field

from infermedica.enums import Sex, AgeUnit, ChoiceId, TriageLevel

class Age(BaseModel):
    value: int = Field(..., ge=0, le=130, description="Wiek pacjenta")
    unit: AgeUnit = AgeUnit.YEAR

class EvidenceItem(BaseModel):
    id: str
    choice_id: ChoiceId
    source: str

class Mention(BaseModel):
    id: str
    choice_id: ChoiceId = ChoiceId.UNKNOWN
    name: str
    common_name: str
    orth: str
    type: str

class Choice(BaseModel):
    id: ChoiceId = ChoiceId.UNKNOWN
    label: str

class QuestionItem(BaseModel):
    id: str
    name: str
    choices: List[Choice]

class Question(BaseModel):
    type: str
    text: str
    extras: Optional[Dict[str, str]]
    items: List[QuestionItem]

class Condition(BaseModel):
    id: str
    name: str
    common_name: str
    probability: float

class ParseRequest(BaseModel):
    age: Age
    sex: Sex
    text: str

class ParseResponse(BaseModel):
    mentions: List[Mention]

class DiagnosisRequest(BaseModel):
    age: Age
    sex: Sex
    evidence: List[EvidenceItem]

class DiagnosisResponse(BaseModel):
    question: Optional[Question] = None
    conditions: List[Condition]

class TriageResponse(BaseModel):
    triage_level: TriageLevel