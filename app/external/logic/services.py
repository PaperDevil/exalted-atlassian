import json

from authlib.integrations.httpx_client import AsyncOAuth2Client
from authlib.oauth2.rfc6749 import OAuth2Token

from app.conf.keys import CONSUMER_KEY, CONSUMER_SECRET
from app.conf.server import HTTPS_HOST_ADDRESS

AUTHORIZE_URL = 'https://bitbucket.org/site/oauth2/authorize'
ACCESS_TOKEN_URL = 'https://bitbucket.org/site/oauth2/access_token'


class BitbucketOAuth2Service:
    oauth = AsyncOAuth2Client(CONSUMER_KEY, CONSUMER_SECRET)

    @classmethod
    async def get_oath_url(cls, user_id: int):
        cls.oauth.redirect_uri = f"{HTTPS_HOST_ADDRESS}/v1/user/auth/{user_id}"
        uri, state = cls.oauth.create_authorization_url(AUTHORIZE_URL)
        return uri

    @classmethod
    async def get_access_token(cls, state: str, code: str) -> OAuth2Token:
        access_token = await cls.oauth.fetch_token(
            ACCESS_TOKEN_URL, state=state, code=code
        )
        return access_token
