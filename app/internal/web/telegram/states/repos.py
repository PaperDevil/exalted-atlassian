from aiogram import types
import aiogram.utils.markdown as fmt

from app.external.drivers.bitbucket import BitbucketDriver
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.logic.services.user import UserService
from app.internal.web.telegram.markups.repos import ReposKeyboard, RepoDetailKeyboard
from app.internal.web.telegram.states.base import BaseStates


class ReposStates(BaseStates):
    def __init__(self):
        self.handlers = {
            '-': self.get_repos,
            'detail': self.detail
        }

    @staticmethod
    async def get_repos(event: types.CallbackQuery, vars: dict):
        user = await UserService.get_user_by_telegram_id(event.from_user.id)
        access_token = await CacheDriver.get_field(user.id, 'access_token')
        repositories: list[BitbucketRepository] = await BitbucketDriver.get_repos(access_token['access_token'])
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
    async def detail(event: types.CallbackQuery, vars: dict):
        uuid: str = vars.get('id')
        user = await UserService.get_user_by_telegram_id(event.from_user.id)
        access_token = await CacheDriver.get_field(user.id, 'access_token')
        repo: BitbucketRepository = await BitbucketDriver.get_repository_by_uuid(access_token['access_token'], uuid)
        keyboard = RepoDetailKeyboard(repo).get_markup()
        await event.message.edit_text(
            text=fmt.text(
                fmt.text(f"**{repo.full_name}**"),
                fmt.text("This is your repository page! From here, you can perform the most basic steps."),
                sep='\n\n'
            )
        )
        await event.message.edit_reply_markup(reply_markup=keyboard)
