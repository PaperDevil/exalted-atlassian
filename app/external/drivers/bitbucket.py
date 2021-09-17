from typing import Optional

import httpx

from app.internal.logic.entities.common.links import BitbucketLinks
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.common.workspace import BitbucketWorkspace

api_url = 'https://bitbucket.org/!api/2.0'


class BitbucketDriver:

    @staticmethod
    async def get_workspaces(access_token: str) -> Optional[list[BitbucketWorkspace]]:
        async with httpx.AsyncClient() as client:
            r = await client.get(api_url + '/workspaces', headers={
                'Authorization': f'Bearer {access_token}'
            })
            data = r.json()
            if len(data) == 0:
                return None
            return [BitbucketWorkspace(
                uuid=workspace.get('uuid'),
                is_private=workspace.get('is_private'),
                name=workspace.get('name')
            ) for workspace in data['values']]

    @staticmethod
    async def get_repos(access_token: str):
        workspaces: list[BitbucketWorkspace] = await BitbucketDriver.get_workspaces(access_token)
        global_repos = []
        for workspace in workspaces:
            repos = await BitbucketDriver.get_repos_for_workspace(access_token, workspace)
            for repo in repos:
                global_repos.append(repo)
        return global_repos

    @staticmethod
    async def get_repos_for_workspace(access_token: str, workspace: BitbucketWorkspace) -> Optional[list[BitbucketRepository]]:
        async with httpx.AsyncClient() as client:
            r = await client.get(api_url + f'/users/{workspace.uuid}/repositories', headers={
                'Authorization': f'Bearer {access_token}'
            })
            data = r.json()
            if len(data) == 0:
                return None
            return [
                BitbucketRepository(
                    uuid=repo.get('uuid'),
                    full_name=repo.get('full_name'),
                    website=repo.get('links')['html']['href'],
                    workspace=workspace,
                    links=BitbucketLinks()
                ) for repo in data['values']
            ]

    @staticmethod
    async def get_repository_by_uuid(access_token: str, uuid: str) -> Optional[BitbucketRepository]:
        async with httpx.AsyncClient() as client:
            r = await client.get(api_url + f'/repositories/{uuid}', headers={
                'Authorization': f'Bearer {access_token}'
            })
            data = r.json()
            if len(data) == 0:
                return None
            repos = await BitbucketDriver.get_repos(access_token)
            for repo in repos:
                if repo.uuid == uuid:
                    return repo
            return None

    @staticmethod
    async def repo_set_webhook(access_token: str, workspace_slug: str, repo_slug: str, uploads: dict):
        async with httpx.AsyncClient() as client:
            uploads.update({
                "skip_cert_verification": True,
                "active": True
            })
            r = await client.post(api_url + f'/repositories/{repo_slug}/hooks',
                                  headers={
                                      'Authorization': f'Bearer {access_token}'
                                  }, json=uploads)
            data = r.json()
            if len(data) == 0:
                return None
            return data.get('active')
