from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.models import StartRequest, AnswerRequest, ResultResponse
from config import INFERMEDICA_APP_ID, INFERMEDICA_API_KEY
from db.database import get_db
from infermedica.client import InfermedicaClient

router = APIRouter(prefix="api/v1/interview", tags=["interview"])

def get_infermedica_client():
    return InfermedicaClient(app_id=INFERMEDICA_APP_ID, app_key=INFERMEDICA_API_KEY)

@router.post("/start")
async def start(
    request: StartRequest,
    db: Session = Depends(get_db),
    client = Depends(get_infermedica_client)
) -> ResultResponse:
    ...

@router.post("{interview_id}/answer")
async def answer(
    interview_id: str,
    request: AnswerRequest,
    db: Session = Depends(get_db),
    client: InfermedicaClient = Depends(get_infermedica_client)
) -> ResultResponse:
    ...
