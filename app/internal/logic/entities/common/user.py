from typing import Optional

from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel
from app.internal.logic.entities.common.links import BitbucketLinks


class BitbucketUser(AbstractRequestModel):
    display_name: Optional[str] = Field(...)
    uuid: Optional[str] = Field(...)
    links: BitbucketLinks
    nickname: Optional[str] = Field(...)
    account_id: Optional[str] = Field(...)
