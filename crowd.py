import base64
import requests


class Crowd:

    def __init__(self, base_url: str, account: tuple[str, str]):
        self._admin_api_base_url = base_url + '/rest/admin/1.0'

        self._session = requests.Session()
        self._session.auth = account


    @classmethod
    def generate_group_id(cls, directory_id: str, group_name: str) -> str:
        # Format of Crowd Group ID and User ID are (Directory ID)-(Group Name or User Name encoded with base64)
        base64_encoded_group_name = base64.b64encode(group_name.encode('utf-8')).decode('utf-8')
        return str(directory_id) + '-' + base64_encoded_group_name
