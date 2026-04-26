from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.endpoints import router
from api.errors import AppError
from db.database import engine, Base
from db import models

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_type": exc.__class__.__name__,
            "message": exc.message
        }
    )

app.include_router(router)
