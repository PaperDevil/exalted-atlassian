from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel


class BitbucketWorkspace(AbstractRequestModel):
    uuid: str = Field(None)
    is_private: bool = Field(None)
    name: str = Field(None)
    slug: str = Field(None)
