import base64
import json
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
    
    
    def get_managed_directories(self) -> list:
        results = list()
        start_index = 0

        while(True):
            # Fetch all Crowd directories by 100.
            response = self._session.get(f'{self._admin_api_base_url}/directory/managed?limit=100&start={start_index}').json()
            results.extend(list(response['values']))

            if response['isLastPage'] == True:
                break
            else:
                start_index = int(response['start']) + int(response['size'])
        
        return results
