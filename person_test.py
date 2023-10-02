import person
import unittest


class TestPerson(unittest.TestCase):

    def test_person(self):
        p1 = person.Person("1", "FNAME", "LNAME")
        self.assertEqual(p1.first_name, "FNAME")
        self.assertEqual(p1.last_name, "LNAME")

    def test_friends(self):
        john = person.Person("1", "John", "Doe")
        james = person.Person("2", "James", "Brown")
        self.assertNotIn(john, james.get_friends())
        james.add_friend(john)
        self.assertIn(john, james.get_friends())

    def test_mutual_friends(self):
        john = person.Person("1", "John", "Doe")
        james = person.Person("2", "James", "Brown")
        jane = person.Person("3", "Jane", "Brown")
        tim = person.Person("4", "Tim", "Cook")
        john.add_friend(james)
        john.add_friend(tim)
        jane.add_friend(james)
        jane.add_friend(john)
        # Remove the [ ] aorund james to create a error
        self.assertEqual(john.find_mutual_friends(jane), [james])

    def test_mutual_friends(self):
        john = person.Person("1", "John", "Doe")
        james = person.Person("2", "James", "Brown")
        jane = person.Person("3", "Jane", "Brown")
        tim = person.Person("4", "Tim", "Cook")
        john.add_friend(james)
        john.add_friend(tim)
        john.add_friend(jane)
        tim.add_friend(john)

        suggested_friends = tim.suggest_friends()
        self.assertIn(james, suggested_friends)
        self.assertIn(jane, suggested_friends)


if __name__ == '__main__':
    unittest.main()
