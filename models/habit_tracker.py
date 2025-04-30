from models.menus import Menus
from views.signup_view import SignupView
from controllers.signup_controller import SignupController
from views.login_view import LoginView
from controllers.login_controller import LoginController
from views.main_view import MainView
from controllers.main_controller import MainController
from data.user_data import Data
from data.update_habits import UpdateHabits

class HabitTracker():
    def __init__(self):
        super().__init__()

        UpdateHabits.update_habits_completed()
        Data.load_data()
        self.make_menus()


    def make_menus(self): 
        # signup menu
        controller = SignupController(view=None)
        signup_menu = SignupView(controller)
        controller.view = signup_menu

        # login menu
        controller = LoginController(view=None)
        login_menu = LoginView(controller)
        controller.view = login_menu

        # main menu
        controller = MainController(view=None)
        main_menu = MainView(controller)
        controller.view = main_menu

        # assign menus 
        Menus.signup_menu = signup_menu
        Menus.login_menu = login_menu
        Menus.main_menu = main_menu
        Menus.current_menu = login_menu

    
    def main_loop(self):
        print("\nWelcome to Habit Tracker app. use \"help\" to see possible commands.\n")
        Menus.current_menu.menu_header()
        while (True):
            Menus.current_menu.handle_input()


            
