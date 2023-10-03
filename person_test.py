import person
import unittest


class TestPerson(unittest.TestCase):

    def test_person(self):
        p1 = person.Person("1", "FNAME", "LNAME")
        self.assertEqual(p1.first_name, "FNAME")
        self.assertEqual(p1.last_name, "LNAME")


if __name__ == '__main__':
    unittest.main()
