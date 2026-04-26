

class AppError(Exception):
    """Bazowa klasa dla błędów aplikacji."""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ExternalAPIError(AppError):
    """Błąd komunikacji z Infermedica."""
    def __init__(self, message: str = "Problem z silnikiem diagnostycznym"):
        super().__init__(message, status_code=502)

class SessionNotFoundError(AppError):
    """Nie znaleziono sesji w bazie."""
    def __init__(self):
        super().__init__("Nie znaleziono sesji wywiadu", status_code=404)

class SessionCompletedError(AppError):
    """Próba modyfikacji zakończonego wywiadu."""
    def __init__(self):
        super().__init__("Ten wywiad został już zakończony", status_code=400)