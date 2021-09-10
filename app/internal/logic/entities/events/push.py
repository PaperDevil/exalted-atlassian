from pydantic import Field

from app.internal.logic.entities.base import AbstractRequestModel
from app.internal.logic.entities.common.links import BitbucketLinks
from app.internal.logic.entities.common.push import BitbucketPushRequest, BitbucketCommit
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.common.user import BitbucketUser


class PushRequestModel(AbstractRequestModel):
    actor: dict = Field(...)
    repository: dict = Field(...)
    push: dict = Field(...)

    def to_model(self) -> BitbucketPushRequest:
        user_links: dict = self.actor.get('links')
        repo_links: dict = self.repository.get('links')
        branch_name: str = 'Undefined🚨'

        push = []
        for change in self.push.get('changes'):
            branch_name = change['new']['name']
            for commit in change['commits']:
                push.append(
                    BitbucketCommit(
                        type=commit.get('type'),
                        message=commit.get('message'),
                        links=BitbucketLinks(
                            html=commit.get('links')['html']['href']
                        )
                    )
                )

        return BitbucketPushRequest(
            actor=BitbucketUser(
                display_name=self.actor.get('display_name'),
                uuid=self.actor.get('uuid'),
                links=BitbucketLinks(
                    self=user_links.get('self').get('href', None),
                    html=user_links.get('html').get('href', None),
                    avatar=user_links.get('avatar').get('href', None)
                ),
                nickname=self.actor.get('nickname'),
                account_id=self.actor.get('account_id')
            ),
            repository=BitbucketRepository(
                uuid=self.repository.get('uuid'),
                full_name=self.repository.get('full_name'),
                website=self.repository.get('website'),
                links=BitbucketLinks(
                    self=repo_links.get('self').get('href', None),
                    html=repo_links.get('html').get('href', None),
                    avatar=repo_links.get('avatar').get('href', None)
                )
            ),
            push=push,
            branch_name=branch_name
        )
