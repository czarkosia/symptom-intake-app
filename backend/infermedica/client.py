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
    Asynchronous HTTP client for communication with Infermedica v3 API.
    Provides methods to access parse, diagnosis and triage endpoints.
    Documentation: https://developer.infermedica.com/documentation/engine-api/
    """

    BASE_URL = "https://api.infermedica.com/v3"

    def __init__(self, app_id: str, app_key: str, interview_id: Optional[str] = None):
        """
        Initializes the Infermedica client with credentials and session state.

        Args:
            app_id (str): Infermedica Application ID.
            app_key (str): Infermedica Application Key.
            interview_id (Optional[str]): Infermedica unique Interview UUID for the current session.
        """
        self.app_id = app_id
        self.app_key = app_key
        self.interview_id = interview_id

    @property
    def headers(self) -> Dict[str, str]:
        """
        Generates required HTTP headers for Infermedica API requests.

        Returns:
            Dict[str, str]: Headers including authentication and session ID.
        """
        h = {
            "App-Id": self.app_id,
            "App-Key": self.app_key,
            "Content-Type": "application/json",
        }
        if self.interview_id is not None:
            h["Interview-Id"] = self.interview_id
        return h

    def set_interview_id(self, new_id: str) -> None:
        """
        Updates the interview ID for the current session.

        Args:
            new_id (str): The new interview session identifier.
        """
        self.interview_id = new_id

    async def _post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Performs an asynchronous POST request to the API.

        Args:
            endpoint (str): The API endpoint path (e.g., '/parse').
            payload (Dict[str, Any]): The JSON request body.

        Returns:
            Dict[str, Any]: The parsed JSON response.

        Raises:
            httpx.HTTPStatusError: If the API returns an error status code.
            httpx.RequestError: If a network-related error occurs.
        """
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
        """
        Retrieves medical mentions from patient's description using infermedica custom NLP system.

        Args:
            data (ParseRequest): Patients basic demographics data with their provided description.

        Returns:
            ParseResponse: Extracted symptoms and risk factors.
        """
        payload = data.model_dump(mode="json", exclude_none=True)

        raw_response = await self._post("/parse", payload)
        return ParseResponse(**raw_response)

    async def diagnosis(self, data: DiagnosisRequest) -> DiagnosisResponse:
        """
        Requests for the next diagnostic question and potential conditions based on evidence.

        Args:
            data (DiagnosisRequest): Patient demographics with previously collected medical evidence.

        Returns:
            DiagnosisResponse: The diagnostic engine's output with further questions if needed
        """
        payload = data.model_dump(mode="json", exclude_none=True)
        payload["extras"] = {"disable_groups": True}

        raw_response = await self._post("/diagnosis", payload)
        return DiagnosisResponse(**raw_response)

    async def triage(self, data: DiagnosisRequest) -> TriageResponse:
        """
        Requests for symptom severity evaluation to determine the appropriate triage level.

        Args:
            data (DiagnosisRequest): Patient demographics and collected evidence.

        Returns:
            TriageResponse: The recommended medical action or severity level.
        """
        payload = data.model_dump(mode="json", exclude_none=True)

        raw_response = await self._post("/triage", payload)
        return TriageResponse(**raw_response)
