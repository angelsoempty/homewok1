import random
class PasswordGenerator:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters
    def generate_password(self):
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

password_generator = PasswordGenerator(8, characters)
print(password_generator.generate_password())
print(password_generator.generate_password())
