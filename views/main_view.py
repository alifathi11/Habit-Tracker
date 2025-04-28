from models.menus import Menus

class MainView:
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.display = """
--------------------------------------
1. Add a new habit 
2. Mark habit as completed
3. View habits & streaks
4. Edit habit
5. Delete habit
6. Export summary
7. Exit
--------------------------------------
"""


    def display_menu(self): 
        print(self.display)

    def handle_input(self):

        self.display_menu()

        try: 
            input_command = int(input())
        except:
            self.show_massage("Invalid command.")
            return

        if input_command == 1:
            habit_name = input("Choose a name for your new habit: ")
            habit_description = input("Write a brief description for your new habit: ")
            self.controller.add_new_habit(habit_name, habit_description)

        elif input_command == 2:
            habit_name = input("Enter the habit name: ")
            self.controller.mark_habit_as_completed(habit_name)

        elif input_command == 3:
            self.controller.view_habits_streaks()

        elif input_command == 4:
            habit_name = input("Enter the habit name: ")
            edit_options_display = """
1. Edit name
2. Edit Description
"""
            try: 
                edit_option = int(input(edit_options_display))
            except: 
                self.show_massage("Invalid command.")
                return
            
            if edit_option == 1:
                new_habit_name = input("Enter the new name: ")
                self.controller.edit_habit_name(new_habit_name)

            elif edit_option == 2:
                new_habit_description = input("Enter the new description: ")
                self.controller.edit_description(new_habit_description)
                
            else:
                self.show_massage("Please choose ether 1 or 2.")
                return

        elif input_command == 5:
            habit_name = input("Enter the habit name: ")
            self.controller.delete_habit()

        elif input_command == 6:
            self.controller.export_summary()

        elif input_command == 7:
            self.controller.exit()
            
        else:
            self.show_massage("Please Enter a Number between 1 and 7")
            return
        
    def show_massage(self, massage):
            print(massage)
        