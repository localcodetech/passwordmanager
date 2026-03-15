from cryptography.fernet import Fernet

from ..ui.signup_page import SignupScreen



class DataEncryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.encryptkey = Fernet(self.key)

        self.datatoken = self.encryptkey.encrypt(
            
        )

