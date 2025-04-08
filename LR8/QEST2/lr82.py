# lr82.py
from user import User
from admin import Admin

user1 = User("Іван", "Іванов", "ivan@example.com", 25)
user2 = User("Марія", "Петрівна", "maria@example.com", 30)

user1.describe_user()
user1.greeting_user()
user2.describe_user()
user2.greeting_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts:", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)

admin = Admin("Admin", "Root", "root@admin.com", 40)
admin.describe_user()
admin.greeting_user()
admin.privileges.show_privileges()
