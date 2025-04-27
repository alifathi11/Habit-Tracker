from models.menus import Menus
from views.register_view import RegisterView
from controllers.register_controller import RegisterController

class HabitTracker():
    def __init__(self):
        super().__init__()
        self.make_menus()


    def make_menus(self): 
        # make register menu
        controller = RegisterController(view=None)
        register_menu = RegisterView(controller)
        controller.view = register_menu

        Menus.current_menu = register_menu
        Menus.register_menu = register_menu

    
    def main_loop(self):

        while (True): #must be changed
            Menus.current_menu.handle_input()


            
