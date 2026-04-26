from typing import List, Optional
from pydantic import BaseModel, Field
from infermedica.enums import Sex, ChoiceId, TriageLevel, AgeUnit
from infermedica.models import Condition, Choice

# Note: In order to simplify the implementation,
# some of the models from infermedica client are reused in interview api.
# In larger projects it is recommended to separate those schemas and map them,
# securing endpoints from changes in external api.

class StartRequest(BaseModel):
    age: int = Field(..., ge=0, le=130)
    age_unit: AgeUnit = AgeUnit.YEAR
    sex: Sex
    text: str

class AnswerRequest(BaseModel):
    item_id: str
    choice_id: ChoiceId

class EvidenceSummaryItem(BaseModel):
    item_id: str
    choice_id: ChoiceId

class QuestionResponse(BaseModel):
    question_text: str
    item_id: str
    name: str
    choices: List[Choice]

class FinalResponse(BaseModel):
    triage_level: TriageLevel
    conditions: List[Condition]

class ResultResponse(BaseModel):
    interview_id: str
    is_finished: bool
    final_response: Optional[FinalResponse] = None
    question_response: Optional[QuestionResponse] = None
    evidence_summary: List[EvidenceSummaryItem]
