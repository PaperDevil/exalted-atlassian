from pydantic import BaseModel, Field


class ExceptionResponse(BaseModel):
    detail: str = Field(..., example='Some message about mistake')
