import string

import secrets


class PasswordGenerator:
    def __init__(self, length):

        self.length = length


    def generation_of_password(self, length):

        self.lowerstrings = string.ascii_lowercase
        self.upperstrings = string.ascii_uppercase
        self.digits       = string.digits
        self.punctuations = string.punctuation

        self.all_charaters = self.lowerstrings+self.upperstrings+self.digits+self.punctuations

        self.length =length


        self.password_generatored = "".join(secrets.choice(self.all_charaters)for _ in range(self.length))

        return self.password_generatored