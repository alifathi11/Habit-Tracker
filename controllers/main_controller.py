from models.menus import Menus
from data.user_data import Data
from datetime import date
from views.redirecting_animation import RedirectingAnimation
import sys, os, csv

class MainController: 
    def __init__(self, view): 
        self.view = view

    def add_new_habit(self, name, description):

        if not name or not description:
            self.view.show_message("\nPlease enter a valid name and description.\n", "bold yellow")
            return
        
        if name in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("\nYou have another habit with this name.\n", "bold red")
            return

        self.save_new_habit(name, description)

        self.view.show_message("\nHabit has been added successfully!\n", "bold green")
    
    def mark_habit_as_completed(self, name):

        if not name:
            self.view.show_message("\nPlease enter the habit name.\n", "bold yellow")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("\nHabit not found.\n", "bold red")
            return
        
        habit = Data.get_current_user_habit(name)
        if habit["completed"] == True:
            self.view.show_message("\nYou have completed this habit for today!\n", "bold yellow")
            return

        habit["completed"] = True
        habit["streak"] += 1
        
        if (habit["streak"] > habit["longest_streak"]):
            habit["longest_streak"] = habit["streak"]
        
        habit["last_check"] = date.today().isoformat()
        self.view.show_message("\nHabit completed!\n", "bold green")


    def view_habits_streaks(self):

        user_habits = Data.get_current_user_habits()
        output = ""
        for habit in user_habits:
            output += f'\nName: {habit["name"]}  ' + ('✅' if habit["completed"] else '❌')
            output += f'\tStreak: {habit["streak"]} | Longest Streak: {habit["longest_streak"]}\n{habit["description"]}\n\n'
        self.view.show_message(output, "white")

    def edit_habit_name(self, old_name, new_name):

        if not old_name: 
            self.view.show_message("\nPlease enter the habit name.\n", "bold yellow")
            return
        
        if old_name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("\nHabit not found.\n", "bold red")
            return
        
        habit = Data.get_current_user_habit(old_name)
        habit["name"] = new_name
        self.view.show_message("\nHabit name edited successfully.\n", "bold green")

    
    def edit_habit_description(self, name, description):

        if not description or not name: 
            self.view.show_message("\nPlease enter the habit name and new description.\n", "bold yellow")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("\nHabit not found.\n", "bold red")
            return
        
        habit = Data.get_current_user_habit(name)
        habit["description"] = description
        self.view.show_message("\nHabit description edited successfully.\n", "bold green")
    
    def delete_habit(self, name):

        if not name: 
            self.view.show_message("\nPlease enter the habit name.\n", "bold yellow")
            return
        
        if name not in [habit["name"] for habit in Data.current_user_habits]:
            self.view.show_message("\nHabit not found.\n", "bold red")
            return

        habits = Data.get_current_user_habits()
        habit = Data.get_current_user_habit(name)
        
        confirmation = input(f'\nDo you want to delete the habit {name}? (Y/n) ').strip().lower()
        if confirmation in ("no", "n"):
            self.view.show_message("\nCancelled.\n", "bold yellow")
            return
        
        elif confirmation in ("yes", "y", ""):
            habits.remove(habit)
            self.view.show_message("\nHabit deleted successfully.\n", "bold green")

        else:
            self.view.show_message("\nInvalid command.\n", "bold red")
            return
        
    def export_summary(self):
        folder_path = "./summary"
        file_path = os.path.join(folder_path, "summary.csv")

        os.makedirs(folder_path, exist_ok=True)

        habits = Data.get_current_user_habits()

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Habit", "Streak", "Longest Streak", "Last Check", "Description"])
            for habit in habits: 
                writer.writerow([habit["name"], habit["streak"], habit["longest_streak"], habit["last_check"], habit["description"]])

        self.view.show_message("Habits exported successfully.", "bold green")


    def exit(self):
        Data.save_change()
        RedirectingAnimation.redirecting_animation("Closing the program")
        sys.exit()
    


    def save_new_habit(self, name, description):

        new_habit = {"name": name, "description": description, "streak": 0, "longest_streak": 0, "completed": False, "last_check": None}
        Data.add_user_habit(new_habit)

    


    
    
    