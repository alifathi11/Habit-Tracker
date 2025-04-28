from models.user import User
from models.menus import Menus
from data.user_data import Data
import json

class SignupController():
    def __init__(self, view): 
        self.view = view

    def signup(self, username, password, email):
        if not username or not password or not email:
            self.view.show_massage("Please Enter a Valid Username, Password and Email Address.")
            return
        
        if username in [user["username"] for user in Data.users]:
            self.view.show_massage("Username already taken.")
            return 
        
        # check validation of username, password and email | TODO
        
        self.save_user_data(username, password, email)
        self.view.show_massage("User created successfully. You are now in Login Menu")
        Menus.switch_menu(self.view, "login menu")

    def save_user_data(self,username, password, email):
        with open('data/users.json', 'r') as file: 
            data_list = json.load(file)
        new_user = {"username": username, "password": password, "email": email}
        data_list.append(new_user)
        Data.add_user(new_user)

        with open('data/users.json', 'w') as file:
            json.dump(data_list, file, indent=4)