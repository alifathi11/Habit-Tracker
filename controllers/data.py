class Data:
    users = {}
    current_user = None
    def __init__(self):
        super().__init__()
    
    def add_user(username, user):
        Data.users[username] = user
    def get_user(username):
        return Data.users.get(username)
    def set_current_user(user):
        Data.current_user = user
    def get_current_user():
        return Data.current_user
    def save_change():
        pass
    def load_users_data():
        pass