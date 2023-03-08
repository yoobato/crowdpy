import base64
import requests

REQUEST_TIMEOUT_IN_SECS = 5


class Crowd:
    '''A class holds many methods which send HTTP requests to Crowd and return the response.

    Args:
        base_url (str): Crowd Base URL (normally ends with /crowd)
        account (str, str): Crowd Account(ID, PW) which has a permission to use API
    
    Attributes:
        _admin_api_base_url (str): Crowd Admin API Base URL (concat with base_url argument)
        _session (requests.Session): Authenticaed Crowd Sesison using HTTP Basic Authentication
    '''

    def __init__(self, base_url: str, account: tuple[str, str]):
        self._admin_api_base_url = base_url + '/rest/admin/1.0'

        self._session = requests.Session()
        self._session.auth = account


    @classmethod
    def generate_group_id(cls, directory_id: str, group_name: str) -> str:
        '''Make Group ID with Directory ID and Group Name

        Crowd's Group ID & User ID have a format as follows: 
            {Directory ID}-Base64Encode({Group Name or User Name})
        
        Args:
            directory_id (str): Crowd Directory ID
            group_name (str): Crowd Group Name
        
        Returns:
            str: Group ID
        '''

        base64_encoded_group_name = base64.b64encode(group_name.encode('utf-8')).decode('utf-8')
        return str(directory_id) + '-' + base64_encoded_group_name 


    def get_managed_directories(self) -> list:
        '''Get all managed directories in Crowd
        
        Returns:
            list: Managed Directories 
        '''

        results = []
        start_index = 0

        while True:
            # Fetch all Crowd directories by 100.
            response = self._session.get(
                f'{self._admin_api_base_url}/directory/managed?limit=100&start={start_index}',
                timeout=REQUEST_TIMEOUT_IN_SECS).json()
            results.extend(list(response['values']))

            if response['isLastPage'] is True:
                break

            start_index = int(response['start']) + int(response['size'])

        return results


    def get_active_users_by_directory(self, directory_id: str) -> list[dict]:
        '''Get all Active users in the given Directory

        Args:
            directory_id (str): Directory's ID where users belong
        
        Returns:
            list: Users
        '''

        results = []
        start_index = 0

        req_data = {
            'directoryIds': [
                directory_id
            ],
            'active': True
        }

        while True:
            # Fetch all Active users in specific directory by 100
            response = self._session.post(
                f'{self._admin_api_base_url}/users/search?limit=100&start={start_index}',
                json=req_data,
                timeout=REQUEST_TIMEOUT_IN_SECS).json()
            results.extend(list(response['values']))

            if response['isLastPage'] is True:
                break

            start_index = int(response['start']) + int(response['size'])

        return results


    def get_users_by_group(self, group_id: str) -> list[dict]:
        '''Get all users in the given Group

        Args:
            group_id (str): Group's ID where users belong
        
        Returns:
            list: Users
        '''

        results = []
        start_index = 0

        while True:
            # Fetch all users in specific group by 100
            response = self._session.get(
                f'{self._admin_api_base_url}/groups/{group_id}/users?limit=100&start={start_index}',
                timeout=REQUEST_TIMEOUT_IN_SECS).json()
            results.extend(list(response['values']))

            if response['isLastPage'] is True:
                break

            start_index = int(response['start']) + int(response['size'])

        return results


    def remove_users_from_group(self, group_id: str, user_ids: list[str]) -> dict[str, list[str]]:
        '''Remove Given users from the given Group

        Args:
            group_id (str): Group's ID where users belong
            user_ids (list of str): Users' ID to remove
        
        Returns:
            dict: User ID list which successfully removed or failed.
        '''

        if len(user_ids) == 0:
            return { 'successes': [], 'failures': [] }

        req_data = { 'ids': user_ids }
        return self._session.delete(
            f'{self._admin_api_base_url}/groups/{group_id}/users',
            json=req_data,
            timeout=REQUEST_TIMEOUT_IN_SECS).json()


    def add_users_to_group(self, group_id: str, user_ids: list[str]) -> dict[str, list[str]]:
        '''Add Given users to the given Group

        Args:
            group_id (str): Group's ID where users will belong
            user_ids (list of str): Users' ID to add
        
        Returns:
            dict: User ID list which successfully added or failed.
        '''

        if len(user_ids) == 0:
            return { 'successes': [], 'failures': [] }

        req_data = { 'ids': user_ids }
        return self._session.post(
            f'{self._admin_api_base_url}/groups/{group_id}/users',
            json=req_data,
            timeout=REQUEST_TIMEOUT_IN_SECS).json()
