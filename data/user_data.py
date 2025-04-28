import json 

class Data:
    users = []
    user_habits = {}
    current_user = None
    current_user_habits = []

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

        if user["username"] in Data.user_habits:
            Data.current_user_habits = Data.user_habits.get(user["username"])

        else:
            Data.user_habits[user["username"]] = []

    def get_current_user():
        return Data.current_user
    
    def get_current_user_habits():
        return Data.current_user_habits
    
    def get_current_user_habit(name):
        for habit in Data.current_user_habits:
            if habit["name"] == name:
                return habit
        return None
    
    def add_user_habit(new_habit):
        Data.current_user_habits.append(new_habit)
    
    def save_change():

        # save user_habits changes
        new_user_habits = Data.user_habits
        new_user_habits[Data.current_user["username"]] = Data.current_user_habits
        with open('data/user_habits.json', 'w') as file:
            json.dump(new_user_habits, file, indent=4)

        # save user data changes
        with open('data/users.json', 'w') as file:
            json.dump(Data.users, file, indent=4)


    def load_data():
        with open('data/users.json', 'r') as file: 
            Data.users = json.load(file)

        with open('data/user_habits.json', 'r') as file:
            Data.user_habits = json.load(file)
            