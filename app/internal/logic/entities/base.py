from pydantic import BaseModel


class AbstractRequestModel(BaseModel):

    class Config:
        use_enum_values = True
