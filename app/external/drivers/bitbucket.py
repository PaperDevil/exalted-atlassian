from typing import Optional

import httpx

from app.internal.logic.entities.common.links import BitbucketLinks
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.common.workspace import BitbucketWorkspace

api_url = 'https://api.bitbucket.org/2.0'


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
            repos = await BitbucketDriver.get_repos_for_workspace(access_token, workspace.uuid)
            for repo in repos:
                global_repos.append(repo)
        return global_repos

    @staticmethod
    async def get_repos_for_workspace(access_token: str, workspace: str) -> Optional[list[BitbucketRepository]]:
        async with httpx.AsyncClient() as client:
            r = await client.get(api_url + f'/users/{workspace}/repositories', headers={
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
