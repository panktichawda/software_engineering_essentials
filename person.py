from typing import List
import dataclasses


@dataclasses.dataclass
class Person:
    user_id: str
    first_name: str
    last_name: str
    friends: List["Person"] = dataclasses.field(default_factory=list)

    def add_friend(self, friend: "Person") -> None:
        if friend not in self.friends:
            self.friends.append(friend)

    def get_friends(self) -> List["Person"]:
        return self.friends

    def find_mutual_friends(self, friend: "Person") -> List["Person"]:
        mutual_friends = []
        my_friends = self.get_friends()
        for friend in friend.get_friends():
            if friend in my_friends:
                mutual_friends.append(friend)
        return mutual_friends
        
    def suggest_friends(self) -> List["Person"]:
        new_friends = list()
        friends = self.get_friends()
        for friend in friends:
            friends_list: List[str] = [
                suggested_friend
                for suggested_friend in friend.get_friends()
                if suggested_friend not in friends and suggested_friend != self and friend not in new_friends
            ]
            new_friends.extend(friends_list)
        
        return new_friends
