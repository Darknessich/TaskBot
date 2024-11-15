import logging
import requests


class YaDisk:
    base_url: str = "https://cloud-api.yandex.net/v1/disk/resources"
    base_path: str = "app%3A%2F"
    __token: str

    def __init__(self, token):
        self.__token = token

    async def upload_file(self, file_name: str, file):
        response = requests.get(
            f"{self.base_url}/upload?path={self.base_path}{file_name}&overwrite=true",
            headers={"Authorization": f"OAuth {self.__token}"},
        )
        if not response.ok:
            logging.error(f"{response.text}")
            raise RuntimeError
        content = response.json()

        response = requests.put(
            content["href"],
            headers={"Authorization": f"OAuth {self.__token}"},
            files={"file": file},
        )
        if not response.ok:
            logging.error(response.text)
            raise RuntimeError

    async def download_file(self, file_name: str, file):
        pass
