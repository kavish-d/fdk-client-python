"""OAuth Client."""

from threading import Timer
from typing import Dict
from urllib import parse
import base64

from ..common.exceptions import FDKOAuthCodeError
from ..common.aiohttp_helper import AiohttpHelper


class OAuthClient:
    def __init__(self, config):
        self._conf = config
        self.token = None
        self.refreshToken = None
        self.retryOAuthTokenTimer = None
        self.raw_token = None
        self.token_expires_in = None

    async def getAccessToken(self):
        return self.token

    async def setToken(self, token):
        self.raw_token = token
        self.token_expires_in = token.get("expires_in")
        self.token = token.get("access_token")
        self.refreshToken = token.get("refresh_token") if token.get("refresh_token") else None
        if self.refreshToken:
            await self.retryOAuthToken(token.get("expires_in"))

    async def retryOAuthToken(self, expires_in):
        if self.retryOAuthTokenTimer:
            self.retryOAuthTokenTimer.cancel()
        if expires_in > 60:
            self.retryOAuthTokenTimer = Timer(float(expires_in - 60), self.renewAccessToken, ())
            self.retryOAuthTokenTimer.start()

    async def startAuthorization(self, options: Dict):
        query = {
          "client_id": self._conf.apiKey,
          "scope": ",".join(options.get("scope", [])),
          "redirect_uri": options.get("redirectUri", ""),
          "state": options.get("state", ""),
          "access_mode": options.get("access_mode", ""),
          "response_type": "code",
        }
        queryString = parse.urlencode(query)
        reqPath = f"/service/panel/authentication/v1.0/company/${self._conf.companyId}/oauth/authorize?{queryString}"
        signingOptions = {
          "method": "GET",
          "host": self._conf.domain,
          "path": reqPath,
          "body": None,
          "headers": {},
          "signQuery": True
        }
        return f"{self._conf.domain}{signingOptions['path']}"

    async def verifyCallback(self, query):
        if query.get("error"):
            raise FDKOAuthCodeError(query.error_description)
        # try:
        res = await self.getAccesstokenObj(grant_type="authorization_code", code=query.get("code", ""))
        await self.setToken(res)
        # except Exception as e:
        #   if error.isAxiosError:
        #     throw new FDKTokenIssueError(error.message)

    async def renewAccessToken(self):
        res = await self.getAccesstokenObj(grant_type="refresh_token", refresh_token=self.refreshToken)
        await self.setToken(res)
        return res

    async def getAccesstokenObj(self, grant_type="", refresh_token="", code=""):
        reqData = {
            grant_type: grant_type,
        }
        if grant_type == "refresh_token":
            reqData = {**reqData, "refresh_token": refresh_token}
        elif grant_type == "authorization_code":
            reqData = {**reqData, "code": code}

        token = base64.b64encode(f"{self._conf.apiKey}:{self._conf.apiSecret}".encode()).decode()
        url = f"{self._conf.domain}/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/token"
        headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = await AiohttpHelper().aiohttp_request("POST", url, reqData, headers)
        return response["json"]

