from typing import Optional

from pydantic import Field, BaseModel

from app.internal.logic.entities.base import AbstractRequestModel

class Link(BaseModel):
    href: Optional[str] = Field(None)

class BitbucketLinks(AbstractRequestModel):
    self: Optional[Link]
    html: Optional[Link]
    avatar: Optional[Link]
