from fastapi import APIRouter

from app.conf.server import CHANNEL_ID
from app.internal.logic.entities.db.user import User
from app.internal.logic.entities.events.push import PushRequestModel
from app.internal.logic.services.push import PushRequestService
from app.internal.logic.services.user import UserService

webhook_router = APIRouter(prefix='/webhook', tags=['Webhook API'])


@webhook_router.post('/')
async def push_repository(request: PushRequestModel):
    await PushRequestService().send_push_event(request.to_model(), CHANNEL_ID)
    return request.actor


@webhook_router.post('/{user_id}')
async def push_repository_user(user_id: int, request: PushRequestModel):
    user: User = await UserService.get_user_by_id(user_id)
    await PushRequestService().send_push_event(request.to_model(), user.telegram_id)
    return request.actor
