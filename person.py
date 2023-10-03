from typing import List
import dataclasses


@dataclasses.dataclass
class Person:
    """Class that holds all info a person."""
    user_id: str
    first_name: str
    last_name: str
    friends: List["Person"] = dataclasses.field(default_factory=list)

    def add_friend(self, friend: "Person") -> None:
        """Add a new friend to this person's friends."""
        if friend not in self.friends:
            self.friends.append(friend)

    def get_friends(self) -> List["Person"]:
        """Returns all friends."""
        return self.friends

    def find_mutual_friends(self, person: "Person") -> List["Person"]:
        """Find common friend between 2 friends."""
        # Implement logic here to find mutual friends between self and person.
        return []

    def suggest_friends(self) -> List["Person"]:
        """Suggest new friend based on current friends."""
        new_friends = list()
        friends = self.get_friends()
        for friend in friends:
            friends_list: List[str] = [
                suggested_friend for suggested_friend in friend.get_friends()
                if suggested_friend not in friends and suggested_friend != self
                and friend not in new_friends
            ]
            new_friends.extend(friends_list)

        return new_friends
