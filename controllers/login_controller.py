from models.user import User
from models.menus import Menus
from controllers.data import Data


class LoginController():
    def __init__(self, view): 
        self.view = view
    
    def login(self, username, password):
        if not username or not password:
            self.view.show_massage("Please Enter a Valid Username and Password.")
            return
        
        if not any(username == username for username in Data.users.keys()): 
            self.view.show_massage("User not found.")
            return 
        
        user = Data.get_user(username)
        correct_password = user.get_password()
        if password != correct_password:
            self.view.show_massage("Password is not correct.")
            return
        
        self.view.show_massage("Login successfully. You are now in Main menu.")
        Data.set_current_user(user)

    def forget_password(self, username, email):
        if not username or not email:
            self.view.show_massage("Please Enter a Valid Username and Email Address.")
            return 
        
        if not any (username == username for username in Data.users.keys()):
            self.view.show_massage("User not found")
            return 

        user = Data.get_user(username)
        correct_email = user.get_email()
        if email != correct_email:
            self.view.show_massage("Email Address is not correct.")
            return 
        
        # logic to send email 
        self.view.show_massage("Check Your Email to Change Your Password!")
        