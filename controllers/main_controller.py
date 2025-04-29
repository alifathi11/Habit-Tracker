from models.user import User
from models.menus import Menus
from data.user_data import Data
from datetime import date
import sys

class MainController: 
    def __init__(self, view): 
        self.view = view

    def add_new_habit(self, name, description):

        if not name or not description:
            self.view.show_message("Please enter a valid name and description.")
            return
        
        if name in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("You have another habit with this name.")
            return

        self.save_new_habit(name, description)

        self.view.show_message("Habit has been added successfully!")
    
    def mark_habit_as_completed(self, name):

        if not name:
            self.view.show_message("Please enter the habit name.")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("Habit not found.")
            return
        
        habit = Data.get_current_user_habit(name)
        if habit["completed"] == True:
            self.view.show_message("You have completed this habit for today!")
            return

        habit["completed"] = True
        habit["streak"] += 1
        habit["last_check"] = date.today().isoformat()
        self.view.show_message("Habit completed!")


    def view_habits_streaks(self):

        user_habits = Data.get_current_user_habits()
        output = ""
        for habit in user_habits:
            output += f'Name: {habit["name"]}  ' + ('✅' if habit["completed"] else '❌')
            output += f'\tStreak: {habit["streak"]}\n{habit["description"]}\n\n'
        self.view.show_message(output)

    def edit_habit_name(self, old_name, new_name):

        if not old_name: 
            self.view.show_message("Please enter the habit name.")
            return
        
        if old_name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("Habit not found.")
            return
        
        habit = Data.get_current_user_habit(old_name)
        habit["name"] = new_name
        self.view.show_message("Habit name edited successfully.")

    
    def edit_habit_description(self, name, description):

        if not description or not name: 
            self.view.show_message("Please enter the habit name and new description.")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("Habit not found.")
            return
        
        habit = Data.get_current_user_habit(name)
        habit["description"] = description
        self.view.show_message("Habit description edited successfully.")
    
    def delete_habit(self, name):

        if not name: 
            self.view.show_message("Please enter the habit name.")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("Habit not found.")
            return

        habits = Data.get_current_user_habits()
        habit = Data.get_current_user_habit(name)
        
        confirmation = input(f'Do you want to delete the habit {name}? (Y/n)').strip().lower()
        if confirmation in ("no", "n"):
            self.view.show_message("Cancelled.")
            return
        
        elif confirmation in ("yes", "y", ""):
            habits.remove(habit)
            self.view.show_message("Habit deleted successfully.")

        else:
            self.view.show_message("Invalid command.")
            return
        
    def export_summary():
        pass

    def exit(self):
        Data.save_change()
        self.view.show_message("Closing the program...")
        sys.exit()
    


    def save_new_habit(self, name, description):

        new_habit = {"name": name, "description": description, "streak": 0, "completed": False, "last_check": None}
        Data.add_user_habit(new_habit)

    


    
    
    