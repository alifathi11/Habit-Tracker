from models.menus import Menus
from rich import print

class SignupView(): 
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.help = """
signup : to create a new account
change menu : to go to login menu
"""

    def display_help(self): 
        print(self.help)

    def menu_header(self):
        self.show_message("================== Signup Menu ==================", "bold blue")

    def handle_input(self):

        input_command = input()

        if input_command.lower() == "signup":

            username = input("Please Enter Your Username: ")
            password = input("Please Enter Your Password: ")
            email = input("Please Enter Your Email Address: ")
            
            self.controller.signup(username, password, email)

        elif input_command.lower() == "change menu":
            menu = input("Enter the menu: (options: Login Menu)\n")
            Menus.switch_menu(self, menu) 

        elif input_command.lower() == "help":
            self.display_help()

        else:
            self.show_message("\nInvalid command.\n", "bold red")

    def show_message(self, massage, style):
            print(f"[{style}]{massage}[/{style}]")