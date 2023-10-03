from flask import Flask
import json, os
from typing import Dict, Any

directory_path = "./users"

app = Flask(__name__)

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
    """Renders a table of all users."""
    user_objs = read_json_files_from_directory(directory_path)
    response = ""
    for person_id in user_objs:
        response += f"""<tr><td><a href="/get_user/{person_id}">{person_id}</a></td></tr>"""
    response = f"""{styles}<table>{response}</table>"""
    return response, 200, {'Content-Type': 'text/html'}


@app.route('/get_user/<string:person_id>', methods=['GET'])
def get_user(person_id):
    """Renders fields of a person with specified person_id."""
    response = ""
    user_objs = read_json_files_from_directory(directory_path)

    if person_id in user_objs:
        person_obj = user_objs[person_id]
        response += f"<tr><td>User ID</td><td>{person_obj['user_id']}</td></tr>"
        response += f"<tr><td>First Name</td><td>{person_obj['first_name']}</td></tr>"
        response += f"<tr><td>Last Name</td><td>{person_obj['last_name']}</td></tr>"
        response += f"""<tr><td>Friends</td><td>{",".join([f"<a href='/get_user/{p}'>{p}</a>" for p in person_obj['friends']])}</td></tr>"""
        response = f"""{styles}<table>{response}</table>"""
        return response, 200, {'Content-Type': 'text/html'}
    else:
        return f"User {person_id} not found."
if __name__ == '__main__':
    app.run()