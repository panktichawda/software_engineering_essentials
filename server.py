from flask import Flask
import os, json, time
import person
import utils
from typing import Dict, Any

directory_path = "./users"
# directory_path = "./users_dummy"

app = Flask(__name__)
person_dict: Dict[str, person.Person] = dict()


@app.route('/')
def get_users():
    """Renders a table of all users."""
    response = ""
    for person_id in person_dict:
        response += f"""<tr><td><a href="/get_user/{person_id}">{person_id}</a></td></tr>"""
    response = f"""{utils.styles}<table>{response}</table>"""
    return response, 200, {'Content-Type': 'text/html'}


@app.route('/get_user/<string:person_id>', methods=['GET'])
def get_user(person_id):
    """Renders fields of a person with specified person_id."""
    response = ""
    if person_id in person_dict:
        person_obj = person_dict[person_id]
        response += f"<tr><td>User ID</td><td>{person_obj.user_id}</td></tr>"
        response += f"<tr><td>First Name</td><td>{person_obj.first_name}</td></tr>"
        response += f"<tr><td>Last Name</td><td>{person_obj.last_name}</td></tr>"
        response += f"""<tr><td>Friends</td><td>{",".join([f"<a href='/get_user/{p.user_id}'>{p.user_id}</a>" for p in person_obj.get_friends()])}</td></tr>"""
        response += f"""<tr><td>Suggested Friends</td><td>{",".join([f"<a href='/get_user/{friend.user_id}'>{friend.user_id}</a>" for friend in person_obj.suggest_friends()]) or "-"}</td></tr>"""
        response = f"""{utils.styles}<table>{response}</table>"""
        return response, 200, {'Content-Type': 'text/html'}
    else:
        return f"User {person_id} not found."


@app.route('/suggest_friends/<string:person_id>', methods=['GET'])
def suggest_friends(person_id):
    """Suggests new friends from current friends."""
    person_obj = person_dict[person_id]
    new_friends = [friend.user_id for friend in person_obj.suggest_friends()]
    return json.dumps({person_obj.user_id: new_friends})


if __name__ == '__main__':
    person_dict = utils.build_users_data(directory_path)
    app.run()
