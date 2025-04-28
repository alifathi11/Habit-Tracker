from models.user import User
from models.menus import Menus
from data.user_data import Data

class MainController: 
    def __init__(self, view): 
        self.view = view

    def add_new_habit(self, name, description):
        if not name or not description:
            self.view.show_massage("Please enter a valid name and description.")
            return
        
        if name in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_massage("You have another habit with this name.")
            return

        save_new_habit(name, description)

        self.view.show_massage("Habit has been added successfully!")


    
    
    