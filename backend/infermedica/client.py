import httpx
import logging
from typing import Dict, Any, Optional
from infermedica.models import (
    ParseRequest,
    ParseResponse,
    DiagnosisRequest,
    DiagnosisResponse,
    TriageResponse
)

logger = logging.getLogger(__name__)

class InfermedicaClient:
    """
    HTTP client for communication with Infermedica v3 API.
    Documentation: https://developer.infermedica.com/documentation/engine-api/
    """

    BASE_URL = "https://api.infermedica.com/v3"

    def __init__(self, app_id: str, app_key: str, interview_id: Optional[str] = None):
        self.app_id = app_id
        self.app_key = app_key
        self.interview_id = interview_id

    @property
    def headers(self) -> Dict[str, str]:
        h = {
            "App-Id": self.app_id,
            "App-Key": self.app_key,
            "Content-Type": "application/json",
        }
        if self.interview_id is not None:
            h["Interview-Id"] = self.interview_id
        return h

    def set_interview_id(self, new_id: str) -> None:
        self.interview_id = new_id

    async def _post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=self.headers)
                response.raise_for_status()  # Wyrzuci błąd dla statusów 4xx i 5xx
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(f"Infermedica API Error: {e.response.status_code} - {e.response.text}")
                raise
            except httpx.RequestError as e:
                logger.error(f"Network error while calling Infermedica: {str(e)}")
                raise

    async def parse(self, data: ParseRequest) -> ParseResponse:
        payload = data.model_dump(mode="json", exclude_none=True)

        raw_response = await self._post("/parse", payload)
        return ParseResponse(**raw_response)

    async def diagnosis(self, data: DiagnosisRequest) -> DiagnosisResponse:
        payload = data.model_dump(mode="json", exclude_none=True)
        payload["extras"] = {"disable_groups": True}

        raw_response = await self._post("/diagnosis", payload)
        return DiagnosisResponse(**raw_response)

    async def triage(self, data: DiagnosisRequest) -> TriageResponse:
        payload = data.model_dump(mode="json", exclude_none=True)

        raw_response = await self._post("/triage", payload)
        return TriageResponse(**raw_response)
