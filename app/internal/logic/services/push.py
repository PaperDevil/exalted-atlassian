from telegram import ParseMode

from app.internal.logic.entities.common.push import BitbucketPushRequest
from app.internal.logic.services.base import BaseService


class PushRequestService(BaseService):

    async def send_push_event(self, push: BitbucketPushRequest, chat_id: str) -> None:
        commits = [f"   - [detail]({commit.links.html}) {commit.message}" for commit in push.push]
        commits.reverse()
        text = (
            f"[{push.actor.nickname}]({push.actor.links.html}) pushing 🔄\n"
            f"Repository: [{push.repository.full_name} 🌐]({push.repository.links.html})\n"
            f"Branch: [{push.branch_name} 🔀]({push.repository.links.html})\n"
            f"Commits:\n" + "".join(commits)
        )

        self.tg.bot.send_message(
            text=text,
            chat_id=chat_id, parse_mode=ParseMode.MARKDOWN)
