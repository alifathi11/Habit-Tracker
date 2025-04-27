from models.user import User
from models.menus import Menus

class RegisterController():
    def __init__(self, view): 
        self.view = view
        self.users = []
    
    def register(self, username, password, email):
        if not username or not password or not email:
            self.view.show_massage("Please Enter a Valid Username, Password and Email Address.")
            return
        
        if any(user.username == username for user in self.users): 
            self.view.show_massage("Username already taken.")
            return 
        
        # check validation of username, password and email | TODO
        
        new_user = User(username, password, email)
        self.users.append(new_user)
        self.view.show_massage("User created successfully. You are now in Login Menu")
        Menus.menu_switcher(Menus.login_menu)