from models.user import User
from models.menus import Menus
from controllers.data import Data

class SignupController():
    def __init__(self, view): 
        self.view = view

    def signup(self, username, password, email):
        if not username or not password or not email:
            self.view.show_massage("Please Enter a Valid Username, Password and Email Address.")
            return
        
        if any(username == username for username in Data.users.keys()): 
            self.view.show_massage("Username already taken.")
            return 
        
        # check validation of username, password and email | TODO
        
        new_user = User(username, password, email)
        Data.add_user(username, new_user)
        self.view.show_massage("User created successfully. You are now in Login Menu")
        Menus.menu_switcher(Menus.login_menu)