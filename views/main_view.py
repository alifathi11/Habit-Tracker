from models.menus import Menus

class MainView:
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.display = """
        1- Habits 
        2- some other things!"""


    def display_menu(self): 
        print(self.display)

    def handle_input(self):

        self.display_menu()

        input_command = input()

        if input_command.lower() == "": #TODO
            pass

        elif input_command.lower() == "change menu":
            menu = input("Enter the menu: (options: Login Menu)\n")
            Menus.switch_menu(self, menu) 

        else:
            self.show_massage("Invalid command.")

    def show_massage(self, massage):
            print(massage)
        