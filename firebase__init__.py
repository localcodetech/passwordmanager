import firebase
import firebase_admin
from firebase_admin import credentials, firestore, auth

from os import path


class FirebaseAdminSDK:
    file_path = path.join("secrets", "vault-password-firebase-adminsdk.json")

    def __init__(self):
        self.secrets = self.file_path
        self.cert = credentials.Certificate(self.secrets)

        self.default_app = firebase_admin.initialize_app(self.cert)


        print(self.default_app.name)

        