# crowdpy

![PyPI](https://img.shields.io/pypi/v/crowdpy)

A Python library for Atlassian Crowd REST API
> Version 1.0.0 and 1.1.0 are for distribution tests and have bugs. Please use crowdpy >= 1.1.1

## Requirements
- Python >= 3.9

## Installation
```sh
pip install crowdpy
```

## Usage
```python
from crowd import Crowd

# Initialize Crowd
crowd = Crowd(base_url: 'https://example.com/crowd', account: (ADMIN_ID, ADMIN_PW))

# Get Directories
directories = crowd.get_managed_directories()
print('Directories :', directories)

# Generate Group ID
group_id = crowd.generate_group_id(directory_id=directories[0]['id'], group_name='TestGroup')
print('Group ID :', group_id)

# Get Users by Group
users = crowd.get_users_by_group(group_id=group_id)
print(f'Users in Group [{group_id}] :', users)
```

## Authors
- [Daeyeol Ryu](https://yoobato.com)

## License
- [Apache License 2.0](./LICENSE)
