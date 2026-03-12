import firebase

from secretskeys.apikeys import ApiKeys

class FirebaseRestApi:
    def __init__(self):
        self.config = {
                        "apiKey": ApiKeys.apiKey,
                        "authDomain": ApiKeys.authDomain,
                        "databaseURL": ApiKeys.dburl,
                        "projectId": ApiKeys.projectId,
                        "storageBucket": ApiKeys.storageBucket,
                        "messagingSenderId": ApiKeys.messagingSenderId,
                        "appId": ApiKeys.appId,
                        "measurementId" : ApiKeys.measurementId
}
    def authentication(self):

        self.auth = firebase.initialize_app(self.config)

        self.app = self.auth.auth()
        
        return self.app