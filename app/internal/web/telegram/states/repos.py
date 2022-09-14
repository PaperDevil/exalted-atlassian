from aiogram import types
import aiogram.utils.markdown as fmt

from app.conf.server import HTTPS_HOST_ADDRESS
from app.external.drivers.bitbucket import BitbucketDriver
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.entities.db.user import User
from app.internal.web.telegram.markups.repos import ReposKeyboard, RepoDetailKeyboard, RepoWebhookKeyboard, \
    RepoJustCloseKeyboard, RepoSettingsKeyboard
from app.internal.web.telegram.states.base import BaseStates
from app.internal.web.telegram.texts.errors import ERROR_CAUGHT_CASE


class ReposStates(BaseStates):
    def __init__(self):
        self.handlers = {
            '-': self.get_repos,
            'detail': self.detail,
            'wh': self.wh,
            'swh': self.swh,
            'settings': self.settings,
            'wsrp': self.workspace_repos
        }

    @staticmethod
    async def workspace_repos(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        """
        Gets all repositories from one workspace
        :payload:
            { slug: str - Workspace Slug (index) }
        """
        repositories = await driver.get_repos_for_workspace_slug(payload.get('slug'))
        keyboard = ReposKeyboard(repositories).get_markup()
        await event.message.edit_text(fmt.text(
            fmt.text("Found few repositories in this workspace."),
            fmt.text("Using the found repositories, you can quickly generate a report based on the latest updates to the repository, or install webhooks with notifications of new pushes or crashes of one of the pipelines."),
            sep='\n\n'
        ))
        await event.message.edit_reply_markup(reply_markup=keyboard)

    @staticmethod
    async def get_repos(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        workspace = await driver.get_account_workspace(await user.account)
        repositories: list[BitbucketRepository] = await driver.get_repos_for_workspace(
            workspace[0]
        )
        keyboard = ReposKeyboard(repositories).get_markup()
        await event.message.edit_text(
            text=fmt.text(
                fmt.text("Several viewable repositories were found in your account."),
                fmt.text("Using the found repositories, you can quickly generate a report based on the latest updates to the repository, or install webhooks with notifications of new pushes or crashes of one of the pipelines."),
                sep='\n\n'
            )
        )
        await event.message.edit_reply_markup(reply_markup=keyboard)

    @staticmethod
    async def detail(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        repo: BitbucketRepository = await driver.get_repository_by_slug(
            workspace=payload.get('ws'),
            slug=payload.get('slug')
        )
        keyboard = RepoDetailKeyboard(repo).get_markup()
        await event.message.edit_text(
            text=fmt.text(
                fmt.text(f"**{repo.full_name}**"),
                fmt.text("This is your repository page! From here, you can perform the most basic steps."),
                sep='\n\n'
            ), parse_mode='Markdown'
        )
        await event.message.edit_reply_markup(reply_markup=keyboard)

    @staticmethod
    async def wh(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        """https://bitbucket.org/bowgroup/sv_telemed_back/admin/webhooks"""
        repo: BitbucketRepository = await driver.get_repository_by_slug(
            workspace=payload.get('workspace'),
            slug=payload.get('slug')
        )
        keyboard = RepoWebhookKeyboard(repo).get_markup()
        await event.message.edit_text(
            text=fmt.text(
                fmt.text("Setup this URL in your repository webhooks:"),
                fmt.text(f"{HTTPS_HOST_ADDRESS}/v1/webhook/{user.id}"),
                sep='\n\n'
            )
        )
        await event.message.edit_reply_markup(reply_markup=keyboard)

    @staticmethod
    async def swh(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        """
        Set Webhook to repository
        :payload:
            {  }
        """
        uuid: str = payload.get('id')
        repo: BitbucketRepository = await BitbucketDriver.get_repository_by_uuid(await user.access_token, uuid)
        success = await BitbucketDriver.repo_set_webhook(
            await user.access_token,
            repo.workspace.name,
            repo.full_name,
            uploads={
                "description": "Exalted Atlassian bot webhook setup",
                "url": f"{HTTPS_HOST_ADDRESS}/v1/webhook/{user.id}",
                "events": [
                    "repo:push"
                ]
            }
        )
        if success:
            await event.message.edit_text(
                text=fmt.text(
                    fmt.text("A webhook has been successfully installed for your repository."),
                    fmt.text("With the next updates to the repository, you will receive a notification about the completion of some event."),
                    fmt.text("To change the notification settings, go to settings -> rules and set the necessary conditions for receiving new notifications."),
                    sep="\n\n"
                )
            )
            await event.message.edit_reply_markup(reply_markup=RepoJustCloseKeyboard().get_markup())
        else:
            await event.message.edit_text(
                text=ERROR_CAUGHT_CASE
            )

    @staticmethod
    async def settings(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        uuid: str = payload.get('id')
        repo: BitbucketRepository = await BitbucketDriver.get_repository_by_uuid(await user.access_token, uuid)
        keyboard = RepoSettingsKeyboard(repo).get_markup()
        await event.message.edit_text(
            text=fmt.text("Using the settings of each repository, you can determine for which events notifications will come and select the branches from which you want to receive notifications."),
            reply_markup=keyboard
        )

    @staticmethod
    async def branches(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        uuid: str = payload.get('id')
