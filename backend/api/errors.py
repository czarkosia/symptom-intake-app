class AppError(Exception):
    """Common application error"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ExternalAPIError(AppError):
    """Infermedica communication error"""
    def __init__(self, message: str = "Infermedica engine API error"):
        super().__init__(message, status_code=502)

class SessionNotFoundError(AppError):
    """Error occurred when session is not found in database"""
    def __init__(self):
        super().__init__("Interview session not found", status_code=404)

class SessionCompletedError(AppError):
    """Error occurred after trying to modify completed interview session"""
    def __init__(self):
        super().__init__("Interview session already completed", status_code=400)