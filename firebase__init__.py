import firebase
import firebase_admin
from firebase_admin import credentials, firestore, auth


class FirebaseAdminSDK:
    def __init__(self):
        self.secrets = ""
        self.cert = credentials.Certificate(self.secrets)

        self.default_app = firebase_admin.initialize_app(self.cert)


        print(self.default_app.name)

        