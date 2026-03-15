import firebase

from secretskeys.apikeys import ApiKeys

class FirebaseRestApi:
    def __init__(self):
        self.config = {
                        "apiKey": "AIzaSyBrUCIM4KyhZRGEThc8dEaIVDjFaY3QVDk",
                        "authDomain": "vault-password.firebaseapp.com",
                        "databaseURL": "https://vault-password-default-rtdb.europe-west1.firebasedatabase.app/",
                        "projectId": "vault-password",
                        "storageBucket": "vault-password.firebasestorage.app",
                        "messagingSenderId":"182265245685",
                        "appId": "1:182265245685:web:4da9de1979f921f1cf7abc",
                        "measurementId" :" G-TMLCLPHG3Z"
}
    def authentication(self):

        self.auth = firebase.initialize_app(self.config)

        self.app = self.auth.auth()
        
        return self.app