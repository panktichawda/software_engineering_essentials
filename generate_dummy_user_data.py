"""This script generates Dummy User(Person) data"""

import json
import names
import os
import random
import sys
from typing import Dict, Any

import person


# Number of users to generate
# Take from arguments or defaults to 10
NUM_USERS = 10
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    NUM_USERS = int(sys.argv[1])
print("Generating dummy data of {} persons....".format(NUM_USERS))

DIRECTORY_PATH = "./users_dummy"

PREFIX = 'Person_'

# This will decide how dense our friendship's graph will be....
# This number should be less than NUM_USERS
MAX_NUMBER_OF_FRIENDS = 8

PERSON_DICT: Dict[str, person.Person] = dict()


# generating users
for i in range(NUM_USERS):
    user_id = PREFIX + str(i)
    # names modle Generates random but "good" names
    PERSON_DICT[user_id] = [{
        "user_id": user_id,
        "first_name": names.get_first_name(),
        "last_name": names.get_last_name(),
        "friends": []
    }]  

# generating friends
for user_id in PERSON_DICT:
    number_of_friends = random.randint(0, MAX_NUMBER_OF_FRIENDS-1)
    friends_to_add = set()
    for j in range(number_of_friends):
        friends_to_add.add(PREFIX + str(random.randint(0, NUM_USERS-1)))
    PERSON_DICT[user_id][0]['friends'] = list(friends_to_add)

os.makedirs(DIRECTORY_PATH, exist_ok = True)
# Saving in dict
for user_id in PERSON_DICT:
    file_path = os.path.join(DIRECTORY_PATH, user_id + '.json')
    with open(file_path, 'w') as json_file:
        json.dump(PERSON_DICT[user_id], json_file)

# print(PERSON_DICT)
print("Done!")