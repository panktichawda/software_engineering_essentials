from flask import Flask
import os
import json
import person
import time
from typing import Dict, Any

directory_path = "./users"
app = Flask(__name__)
person_dict: Dict[str, person.Person] = dict()
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


# Function to read JSON content from a directory
def read_json_files_from_directory(directory_path: str):
    json_data: Dict[str, Any] = {}

    try:
        # Iterate through the files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.json'):
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


@app.route('/')
def get_users():
    response = ""
    for person_id in person_dict:
        response += f"""<tr><td><a href="/get_user/{person_id}">{person_id}</a></td></tr>"""
    response = f"""{styles}<table>{response}</table>"""
    return response, 200, {'Content-Type': 'text/html'}


@app.route('/get_user/<string:person_id>', methods=['GET'])
def get_user(person_id):
    response = ""
    if person_id in person_dict:
        person_obj = person_dict[person_id]
        response += f"<tr><td>User ID</td><td>{person_obj.user_id}</td></tr>"
        response += f"<tr><td>First Name</td><td>{person_obj.first_name}</td></tr>"
        response += f"<tr><td>Last Name</td><td>{person_obj.last_name}</td></tr>"
        response += f"""<tr><td>Friends</td><td>{",".join([f"<a href='/get_user/{p.user_id}'>{p.user_id}</a>" for p in person_obj.get_friends()])}</td></tr>"""
        response += f"""<tr><td>Suggested Friends</td><td>{",".join([f"<a href='/get_user/{friend.user_id}'>{friend.user_id}</a>" for friend in person_obj.suggest_friends()]) or "-"}</td></tr>"""
        response = f"""{styles}<table>{response}</table>"""
        return response, 200, {'Content-Type': 'text/html'}
    else:
        return f"User {person_id} not found."


@app.route('/suggest_friends/<string:person_id>', methods=['GET'])
def suggest_friends(person_id):
    person_obj = person_dict[person_id]
    new_friends = [friend.user_id for friend in person_obj.suggest_friends()]
    return json.dumps({person_obj.user_id: new_friends})

def build_users_data():
    user_data = read_json_files_from_directory(directory_path)
    # time.sleep(10)
    for user_id, user_info in user_data.items():
        person_obj = person.Person(user_id=user_id,
                                   first_name=user_info['first_name'],
                                   last_name=user_info['last_name'])
        person_dict[user_id] = person_obj
    for user_id, user_info in user_data.items():
        for friend_id in user_info['friends']:
            person_dict[user_id].add_friend(person_dict[friend_id])
 
if __name__ == '__main__':
    build_users_data()ser
    app.run()
    
