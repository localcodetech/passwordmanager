import firebase

from secretskeys.apikeys import ApiKeys

class FirebaseRestApi:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.config = {
                        "apiKey": ApiKeys.apiKey,
                        "authDomain": ApiKeys.authDomain,
                        "databaseURL": ApiKeys.dburl,
                        "projectId": ApiKeys.projectId,
                        "storageBucket": ApiKeys.storageBucket,
                        "messagingSenderId": ApiKeys.messagingSenderId,
                        "appId": ApiKeys.appId,
                        "measurementId" :ApiKeys.measurementId
        }

    

        self.app = firebase.initialize_app(self.config)

        self.auth = self.app.auth()
        
        
    

    def login_func(self):
        self.user = self.auth.sign_in_with_email_and_password(email=self.email, password=self.password)
        return self.user
    

    def signup_func(self):
        signup = self.auth.create_user_with_email_and_password(email=self.email, password=self.password)
        return signup
    

