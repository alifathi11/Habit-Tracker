from models.user import User
from models.menus import Menus
from data.user_data import Data


class LoginController():
    def __init__(self, view): 
        self.view = view
    
    def login(self, username, password):
        if not username or not password:
            self.view.show_message("Please Enter a Valid Username and Password.")
            return
        
        if username not in [user["username"] for user in Data.users]:
            self.view.show_message("User not found.")
            return 
        
        user = Data.get_user(username)
        correct_password = user["password"]
        if password != correct_password:
            self.view.show_message("Password is not correct.")
            return
        
        self.view.show_message("Login successfully. You are now in Main menu.")
        Menus.switch_menu(self.view, "main menu")
        Data.set_current_user(user)

    def forget_password(self, username, email):
        if not username or not email:
            self.view.show_message("Please Enter a Valid Username and Email Address.")
            return 
        
        if username not in [user["username"] for user in Data.users]:
            self.view.show_message("User not found")
            return 

        user = Data.get_user(username)
        correct_email = user["email"]
        if email != correct_email:
            self.view.show_message("Email Address is not correct.")
            return 
        
        # logic to send email 
        self.view.show_message("Check Your Email to Change Your Password!")
        