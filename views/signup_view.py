from models.menus import Menus

class SignupView(): 
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

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

        else:
            self.show_message("Invalid command.")

    def show_message(self, massage):
            print(massage)