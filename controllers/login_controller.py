from models.menus import Menus
from data.user_data import Data
from controllers.email_sender import EmailSender


class LoginController():
    def __init__(self, view): 
        self.view = view
    
    def login(self, username, password):
        if not username or not password:
            self.view.show_message("\nPlease Enter a Valid Username and Password.\n", "bold yellow")
            return
        
        if username not in [user["username"] for user in Data.users]:
            self.view.show_message("\nUser not found.\n", "bold red")
            return 
        
        user = Data.get_user(username)
        correct_password = user["password"]
        if password != correct_password:
            self.view.show_message("\nPassword is not correct.\n", "bold red")
            return
        
        self.view.show_message("\nLogin successfully.\n", "bold green")
        Menus.switch_menu(self.view, "main menu")
        Data.set_current_user(user)

    def forget_password(self, username, email):
        if not username or not email:
            self.view.show_message("\nPlease Enter a Valid Username and Email Address.\n", "bold yellow")
            return 
        
        if username not in [user["username"] for user in Data.users]:
            self.view.show_message("\nUser not found\n", "bold red")
            return 

        user = Data.get_user(username)
        correct_email = user["email"]
        if email != correct_email:
            self.view.show_message("\nEmail Address is not correct.\n", "bold red")
            return 
        
        user_password = user["password"]
        EmailSender.send_email(email, self.view, "Forget Password", f"Your Password: {user_password}")
        
        
        