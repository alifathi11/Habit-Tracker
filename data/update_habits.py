import json
from datetime import datetime, date, timedelta

class UpdateHabits:
    def __init__(self):
        super().__init__()
    
    def update_habits_completed():

        today = date.today()

        updated_user_habits = {}
        with open('data/user_habits.json', 'r') as file: 
            updated_user_habits = json.load(file)

        for user_habit in updated_user_habits:

            habits = updated_user_habits[user_habit]

            for habit in habits:

                habit_last_check = habit["last_check"]
            
                if (habit_last_check != None):

                    habit_last_check_date = datetime.strptime(habit["last_check"], "%Y-%m-%d").date()

                    if habit_last_check_date + timedelta(habit["frequency"]) < today:
                        habit["completed"] = False
                    if habit_last_check_date + timedelta(habit["frequency"]) + timedelta(habit["frequency"]) < today:
                        habit["streak"] = 0
                        
        

        with open('data/user_habits.json', 'w') as file:
            json.dump(updated_user_habits, file, indent=4)