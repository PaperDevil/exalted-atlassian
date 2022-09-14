from typing import Optional, List

import httpx

from app.internal.logic.entities.common.links import BitbucketLinks
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.common.user import BitbucketUser
from app.internal.logic.entities.common.workspace import BitbucketWorkspace

API_URL = 'https://api.bitbucket.org/2.0'


class BitbucketDriver:

    def __init__(self, access_token: str):
        self.URL = API_URL
        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }

    async def get_current_user(self) -> Optional[BitbucketUser]:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + '/user', headers=self.headers)
            data = r.json()
            return BitbucketUser(**data)

    async def get_workspace(self, slug) -> Optional[BitbucketWorkspace]:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + f'/workspaces/{slug}', headers=self.headers)
            data = r.json()
            return BitbucketWorkspace(**data)

    async def get_account_workspace(self, account: BitbucketUser) -> List[BitbucketWorkspace]:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + f'/user/permissions/workspaces',
                                 headers=self.headers,
                                 params={'q': 'permission="owner"'})
            data = r.json()
            return [BitbucketWorkspace(**ws['workspace']) for ws in data['values']
                    if ws['workspace']['name'] == account.nickname]

    async def get_workspaces(self) -> Optional[list[BitbucketWorkspace]]:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + '/workspaces', headers=self.headers)
            data = r.json()
            if len(data) == 0:
                return None
            return [BitbucketWorkspace(
                uuid=workspace.get('uuid'),
                is_private=workspace.get('is_private'),
                name=workspace.get('name'),
                slug=workspace.get('slug')
            ) for workspace in data['values']]

    async def get_repos(self):
        workspaces: list[BitbucketWorkspace] = await self.get_workspaces()
        global_repos = []
        for workspace in workspaces:
            repos = await self.get_repos_for_workspace(workspace)
            for repo in repos:
                global_repos.append(repo)
        return global_repos

    async def get_repos_for_workspace(self, workspace: BitbucketWorkspace) -> Optional[list[BitbucketRepository]]:
        return await self.get_repos_for_workspace_slug(workspace.slug)

    async def get_repos_for_workspace_slug(self, workspace_slug: str) -> List[BitbucketRepository]:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + f'/repositories/{workspace_slug}', headers=self.headers)
            data = r.json()
            return [
                BitbucketRepository(
                    uuid=repo.get('uuid'),
                    full_name=repo.get('full_name'),
                    website=repo.get('links')['html']['href'],
                    slug=repo.get('slug'),
                    workspace=BitbucketWorkspace(
                        slug=workspace_slug
                    ),
                    links=BitbucketLinks()
                ) for repo in data['values']
            ]

    async def get_repository_by_slug(self, workspace: str, slug: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.URL + f'/repositories/{workspace}/{slug}', headers=self.headers)
            data = r.json()
            if len(data) == 0:
                return None
            return BitbucketRepository(**data)

    async def repo_set_webhook(self, workspace_slug: str, repo_slug: str, uploads: dict):
        async with httpx.AsyncClient() as client:
            uploads.update({
                "skip_cert_verification": True,
                "active": True
            })
            r = await client.post(self.URL + f'/repositories/{repo_slug}/hooks',
                                  headers=self.headers, json=uploads)
            data = r.json()
            if len(data) == 0:
                return None
            return data.get('active')
