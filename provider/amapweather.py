from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
import requests

class AmapweatherProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            #获得用户提供的Amap_apikey
            api_key = credentials['amap_apikey']

            #发送一个请求测试
            url = "https://restapi.amap.com/v3/weather/weatherInfo"
            params = {
                "key": api_key,  # 使用获取到的API Key
                "city": 410526,
                "extensions": "base",  # 基础天气信息
                "output": "json"
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # 抛出HTTP错误
            result = response.json()
            status = result["status"]
            if status != "1":
                # 当status不等于1时，获取错误信息并报错
                error_info = result["info"]
                raise ToolProviderCredentialValidationError(f"apikey验证失败，请确定apikey是否正确: {error_info}")
            else:
                pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))

    #########################################################################################
    # If OAuth is supported, uncomment the following functions.
    # Warning: please make sure that the sdk version is 0.4.2 or higher.
    #########################################################################################
    # def _oauth_get_authorization_url(self, redirect_uri: str, system_credentials: Mapping[str, Any]) -> str:
    #     """
    #     Generate the authorization URL for amapweather OAuth.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR AUTHORIZATION URL GENERATION HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return ""
        
    # def _oauth_get_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], request: Request
    # ) -> Mapping[str, Any]:
    #     """
    #     Exchange code for access_token.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR CREDENTIALS EXCHANGE HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return dict()

    # def _oauth_refresh_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], credentials: Mapping[str, Any]
    # ) -> OAuthCredentials:
    #     """
    #     Refresh the credentials
    #     """
    #     return OAuthCredentials(credentials=credentials, expires_at=-1)
