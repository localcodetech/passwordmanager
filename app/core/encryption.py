from cryptography.fernet import Fernet





class DataEncryption:
    def __init__(self, database_config):

        self.database = database_config

        self.key = Fernet.generate_key()
        self.encryptkey = Fernet(self.key)

        

        


    def encrytion_func(self):    
        
        self.key = Fernet.generate_key()
        self.encryptkey = Fernet(self.key)

        datatoken = self.encryptkey.encrypt(self.database)

        return datatoken

    def decryption(self, datatoken):

        self.decryt_data = self.encryptkey.decrypt(datatoken)
        self.password_final = self.decryt_data.decode("utf-8")

        return self.password_final



