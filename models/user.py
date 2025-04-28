class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_email(self):
        return self.email