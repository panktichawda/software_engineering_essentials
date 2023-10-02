from typing import Dict, Any
import json, os
import person

# Styles for html tables in response
styles = """
    <style>
        table {
            border-collapse: collapse;
        }
        tr, td{
            border: 1px solid black;
            padding: 5px;
            text-align: center;
        }
        body{
        align: center
        }
    </style>
"""


def read_json_files_from_directory(directory_path: str):
    """ Read JSON files from provided path and return dict in format of {user_id:user_info}"""
    json_data: Dict[str, Any] = {}

    try:
        # Iterate through the files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.json') and filename.find(
                    'enrollment_id') == -1:
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:
                    # Read and parse the JSON data
                    data = json.load(file)
                    for user_info in data:
                        json_data[user_info["user_id"]] = user_info
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    return json_data


def convert_json_to_objects(
        user_data: Dict[str, Any]) -> Dict[str, person.Person]:
    """Create class object from provided json data."""

    user_dict: Dict[str, person.Person] = dict()
    for user_id, user_info in user_data.items():
        person_obj = person.Person(user_id=user_id,
                                   first_name=user_info['first_name'],
                                   last_name=user_info['last_name'])
        user_dict[user_id] = person_obj
    return user_dict


def create_friend_connections(user_data: Dict[str, Any],
                              user_dict: Dict[str, person.Person]):
    """"Create connections between friends by reading from JSON data."""
    for user_id, user_info in user_data.items():
        for friend_id in user_info['friends']:
            user_dict[user_id].add_friend(user_dict[friend_id])


def build_users_data(dir_path: str) -> Dict[str, person.Person]:
    """"Given a dir path, create object and friend connections."""
    user_data = read_json_files_from_directory(dir_path)

    user_dict = convert_json_to_objects(user_data)

    create_friend_connections(user_data, user_dict)

    return user_dict
