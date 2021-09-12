from fastapi import APIRouter

from app.conf.server import CHANNEL_ID
from app.internal.logic.entities.events.push import PushRequestModel
from app.internal.logic.services.push import PushRequestService

webhook_router = APIRouter(prefix='/webhook', tags=['Webhook API'])


@webhook_router.post('/')
async def push_repository(request: PushRequestModel):
    await PushRequestService().send_push_event(request.to_model(), CHANNEL_ID)
    return request.actor
