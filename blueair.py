import requests
import base64
import logging
import config


class NoLoginError(Exception):
    pass


class BlueAir:

    def __init__(self):
        self.host = "api-us-east-1.foobot.io"
        self.auth = "Basic " + base64.encodebytes(bytes(f"{config.email}:{config.password}", "utf-8")).decode().rstrip('\n')
        self.headers = {
            'X-API-KEY-TOKEN': config.api_token,
            'Authorization': self.auth,
            'Cache-Control': "no-cache",
            'Content-Type': "application/json"
            }
        self.login()

    def _get(self, path):
        url = f"https://{self.host}{path}"
        return requests.request("GET", url, headers=self.headers)

    def _post(self, path, data):
        url = f"https://{self.host}{path}"
        return requests.request("POST", url, headers=self.headers, json=data)

    def login(self):
        res = self._get(f"/v2/user/{config.email}/login/")
        logging.info(res.headers)
        logging.info(res.text)
        self.headers['X-AUTH-TOKEN'] = res.headers['X-AUTH-TOKEN']

    def check_login_status(self):
        if 'X-AUTH-TOKEN' not in self.headers:
            raise NoLoginError()

    def get_account_info(self):
        return self._get(f"/v2/user/{config.email}/get/")

    def get_device_info(self):
        return self._get(f"/v2/owner/{config.email}/device/").json()

    def set_fan(self, uuid, level):
        data = {
                "currentValue": f"{level}",
                "scope": "device",
                "defaultValue": f"{level}",
                "name": "fan_speed",
                "uuid": f"{uuid}"
            }
        self._post(f"/v2/device/{uuid}/attribute/fanspeed/", data)
