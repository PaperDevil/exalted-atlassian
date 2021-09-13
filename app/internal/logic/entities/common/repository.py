from typing import Optional

from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel
from app.internal.logic.entities.common.links import BitbucketLinks


class BitbucketRepository(AbstractRequestModel):
    uuid: Optional[str] = Field(None)
    full_name: Optional[str] = Field(None)
    website: Optional[str] = Field(None)
    links: BitbucketLinks
