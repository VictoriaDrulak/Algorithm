class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

    def greeting_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()


user1 = User("John", "Doe", "john.doe@example.com", 30)
user1.describe_user()
user1.greeting_user()
print()

user2 = User("Alice", "Smith", "alice.smith@example.com", 25)
user2.describe_user()
user2.greeting_user()
print()

user3 = User("Bob", "Johnson", "bob.johnson@example.com", 35)
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f"Login attempts for {user3.first_name}: {user3.login_attempts}")
user3.reset_login_attempts()
print(f"After reset, login attempts for {user3.first_name}: {user3.login_attempts}")
print()

admin = Admin("Admin", "Super", "admin@example.com", 40)
admin.privileges.privileges = [
    "Allowed to add message",
    "Allowed to delete users",
    "Allowed to ban users"
]
admin.show_privileges()
print()

from admin import Admin

admin_imported = Admin("Imported", "Admin", "imported.admin@example.com", 35)
admin_imported.privileges.privileges = [
    "Allowed to add message",
    "Allowed to delete users",
    "Allowed to ban users"
]
admin_imported.show_privileges()