from fastapi import APIRouter

from app.external.entities.exception_response import ExceptionResponse
from app.internal.web.http.api.webhook import webhook_router

general_router = APIRouter(prefix='/v1', responses={400: {'model': ExceptionResponse},
                                                    500: {'model': ExceptionResponse}})

general_router.include_router(webhook_router)
