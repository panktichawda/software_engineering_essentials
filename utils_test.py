import person
import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_convert_json_to_objects(self):
        user_data = {
            "user1": {
                "user_id": "user1",
                "first_name": "fname",
                "last_name": "lname",
                "friends": []
            }
        }
        user_dict = utils.convert_json_to_objects(user_data)
        self.assertIn('user1', user_dict)
        self.assertEqual(user_dict['user1'].user_id, "user1")
        self.assertEqual(user_dict['user1'].first_name, "fname")
        self.assertEqual(user_dict['user1'].last_name, "lname")

    def test_create_friend_connections(self):
        user_data = {
            "user1": {
                "user_id": "user1",
                "first_name": "fname1",
                "last_name": "lname1",
                "friends": ["user2"]
            },
            "user2": {
                "user_id": "user2",
                "first_name": "fname2",
                "last_name": "lname2",
                "friends": ["user1"]
            }
        }
        user_dict = utils.convert_json_to_objects(user_data)
        self.assertEqual(user_dict['user1'].get_friends(), [])
        self.assertEqual(user_dict['user2'].get_friends(), [])

        utils.create_friend_connections(user_data, user_dict)

        self.assertEqual(user_dict['user1'].get_friends(), [user_dict['user2']])
        self.assertEqual(user_dict['user2'].get_friends(), [user_dict['user1']])


if __name__ == '__main__':
    unittest.main()
