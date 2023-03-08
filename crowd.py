import requests


class Crowd:

    def __init__(self, base_url: str, account: tuple[str, str]):
        self._admin_api_base_url = base_url + '/rest/admin/1.0'

        self._session = requests.Session()
        self._session.auth = account
