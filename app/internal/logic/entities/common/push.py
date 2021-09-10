from typing import Optional, List

from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel
from app.internal.logic.entities.common.links import BitbucketLinks
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.common.user import BitbucketUser


class BitbucketCommit(AbstractRequestModel):
    type: Optional[str] = Field(None)
    message: Optional[str] = Field(None)
    links: BitbucketLinks


class BitbucketPushRequest(AbstractRequestModel):
    actor: BitbucketUser
    repository: BitbucketRepository
    push: List[BitbucketCommit]
    branch_name: Optional[str] = Field(None)
