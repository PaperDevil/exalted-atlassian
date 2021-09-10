from typing import Optional

from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel


class BitbucketLinks(AbstractRequestModel):
    self: Optional[str] = Field(None)
    html: Optional[str] = Field(None)
    avatar: Optional[str] = Field(None)
