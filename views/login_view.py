from models.menus import Menus
from rich import print
class LoginView(): 
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.help = """
login : to login to your account
forget password : if you've forgotten your password
change menu : to go to signup menu
"""

    def display_help(self): 
        print(self.help)

    def menu_header(self):
        self.show_message("================== Login Menu ==================", "bold blue")

    def handle_input(self):

        input_command = input()

        if input_command.lower() == "login":

            username = input("Please Enter Your Username: ")
            password = input("Please Enter Your Password: ")
            
            self.controller.login(username, password)
        
        elif input_command.lower() == "forget password":
            username = input("Please Enter Your Username: ")
            email = input("Please Enter Your Email Address: ")
            
            self.controller.forget_password(username, email)

        elif input_command.lower() == "change menu":
            menu = input("Enter the menu: (options: Signup Menu)\n")
            Menus.switch_menu(self, menu)   

        elif input_command.lower() == "help":
            self.display_help()

        else:
            self.show_message("\nInvalid command.\n", "bold red")

    def show_message(self, massage, style):
            print(f"[{style}]{massage}[/{style}]")