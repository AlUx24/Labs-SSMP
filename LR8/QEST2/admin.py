# admin.py
from user import User

class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("-", privilege)

class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()
