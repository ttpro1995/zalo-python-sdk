class APIConfig:
    DEFAULT_OA_API_VERSION = "v1"
    DEFAULT_3RDAPP_API_VERSION = "v2.0"
    DEFAULT_OA_API_BASE = "https://openapi.zaloapp.com/oa"
    USER_AGENT = "zalosdk/1.0 Zalo Open API Python SDK"
    SDK_VERSION = "Python 1.0"
    SDK_SOURCE = "PythonSDK-1.0"

    @staticmethod
    def create_default_header():
        header = {
            "User-Agent": APIConfig.USER_AGENT,
            "SDK_VERSION": APIConfig.SDK_VERSION,
            "SDK-Source": APIConfig.SDK_SOURCE,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return header