from models.menus import Menus
from data.user_data import Data
import re

class SignupController():
    def __init__(self, view): 
        self.view = view

    def signup(self, username, password, email):
        if not username or not password or not email:
            self.view.show_message("\nPlease Enter a Valid Username, Password and Email Address.\n", "bold yellow")
            return
        
        if username in [user["username"] for user in Data.users]:
            self.view.show_message("\nUsername already taken.\n", "bold red")
            return 
        
        if not self.is_valid(username, password, email):
            return
        
        self.save_user_data(username, password, email)
        self.view.show_message("\nUser created successfully.\n", "bold green")
        Menus.switch_menu(self.view, "login menu")

    def save_user_data(self,username, password, email):
        new_user = {"username": username, "password": password, "email": email}
        Data.add_user(new_user)

    
    def is_valid(self, username, password, email):

        username_pattern = r"^[a-zA-Z0-9](?:[a-zA-Z0-9_]{3,}[a-zA-Z0-9])$"
        password_pattern = r"^(?=.*[A-Za-z])(?=.*[\d!@#$%^&*()_+=\-[\]{}|;:',.<>?/])[A-Za-z\d!@#$%^&*()_+=\-[\]{}|;:',.<>?/]{8,}$"
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.fullmatch(username_pattern, username):
            self.view.show_message("\nUsername format is not valid.\n", "bold red")
            return False
    
        if not re.fullmatch(password_pattern, password):
            self.view.show_message("\nPassword format is not valid.\n", "bold red")
            return False

        if not re.fullmatch(email_pattern, email):
            self.view.show_message("\nEmail Address format is not valid.\n", "bold red")
            return False
        
        return True

