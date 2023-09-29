import person

class TestPerson:

    def test_person(self):
        p1 = person.Person("1", "FNAME", "LNAME")
        assert p1.first_name == "FNAME"
        assert p1.last_name == "LNAME"

    def test_friends(self):
        john = person.Person("1", "John", "Doe")
        james = person.Person("2", "James", "Brown")
        assert john not in james.get_friends()
        james.add_friend(john)
        assert john in james.get_friends()

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
        assert john.find_mutual_friends(jane) == [james]

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
        
        assert james in suggested_friends
        assert jane in suggested_friends