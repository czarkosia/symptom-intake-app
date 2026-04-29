from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.models import StartRequest, AnswerRequest, ResultResponse
from api.service import InterviewService
from config import INFERMEDICA_APP_ID, INFERMEDICA_APP_KEY
from db.database import get_db
from infermedica.client import InfermedicaClient

router = APIRouter(prefix="/api/v1/interview", tags=["interview"])

def get_infermedica_client():
    return InfermedicaClient(app_id=INFERMEDICA_APP_ID, app_key=INFERMEDICA_APP_KEY)

def get_interview_service(
    db: Session = Depends(get_db),
    client: InfermedicaClient = Depends(get_infermedica_client)
):
    return InterviewService(db=db, client=client)

@router.post("/start")
async def start(
    request: StartRequest,
    service: InterviewService = Depends(get_interview_service)
) -> ResultResponse:
    return await service.start_interview(request)

@router.post("/answer")
async def answer(
    request: AnswerRequest,
    service: InterviewService = Depends(get_interview_service)
) -> ResultResponse:
    return await service.process_answer(request)
