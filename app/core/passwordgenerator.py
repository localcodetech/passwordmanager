import string

import secrets


class PasswordGenerator:
    def __init__(self):
        pass


    def generator(self, length):

        self.lowerstrings = string.ascii_lowercase
        self.upperstrings = string.ascii_uppercase
        self.digits       = string.digits
        self.punctuations = string.punctuation

        self.all_charaters = self.lowerstrings+self.upperstrings+self.digits+self.punctuations

        self.length =length


        self.password_generatored = "".join(secrets(self.all_charaterssecret)for _ in range(self.length))

        return self.password_generatored