import json 

class Data:
    users = []
    user_habits = {}
    current_user = None

    def __init__(self):
        super().__init__()
    
    def add_user(user):
        Data.users.append(user)

    def get_user(username):
        for user in Data.users: 
            if user["username"] == username:
                return user
            
    def set_current_user(user):
        Data.current_user = user

    def get_current_user():
        return Data.current_user
    
    def save_change():
        pass

    def load_users_data():
        with open('data/users.json', 'r') as file: 
            Data.users = json.load(file)

        with open('data/user_habits.json', 'r') as file:
            Data.user_habits = json.load(file)
            