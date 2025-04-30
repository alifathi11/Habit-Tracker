from models.menus import Menus
from rich import print

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

    def menu_header(self):
        self.show_message("================== Main Menu ==================", "bold blue")

    def handle_input(self):

        input_command = input()
        if input_command.lower() == "help":
            self.display_menu()
        try: 
            input_number = int(input_command)
        except:
            self.show_message("\nInvalid command.\n", "bold red")
            return

        if input_number == 1:
            habit_name = input("\nChoose a name for your new habit: ")
            habit_description = input("Write a brief description for your new habit: ")
            habit_frequency = input("Enter the frequency in days: ")
            self.controller.add_new_habit(habit_name, habit_description, habit_frequency)

        elif input_number == 2:
            habit_name = input("Enter the habit name: ")
            self.controller.mark_habit_as_completed(habit_name)

        elif input_number == 3:
            self.controller.view_habits_streaks()

        elif input_number == 4:
            habit_name = input("Enter the habit name: ")
            edit_options_display = """
1. Edit name
2. Edit Description
"""
            try: 
                edit_option = int(input(edit_options_display))
            except:
                self.show_message("\nInvalid command.\n", "bold red")
                return
            
            if edit_option == 1:
                new_habit_name = input("Enter the new name: ")
                self.controller.edit_habit_name(habit_name, new_habit_name)

            elif edit_option == 2:
                new_habit_description = input("Enter the new description: ")
                self.controller.edit_habit_description(habit_name, new_habit_description)
                
            else:
                self.show_message("\nPlease choose ether 1 or 2.\n", "bold yellow")
                return

        elif input_number == 5:
            habit_name = input("Enter the habit name: ")
            self.controller.delete_habit(habit_name)

        elif input_number == 6:
            self.controller.export_summary()

        elif input_number == 7:
            self.controller.exit()
            
        else:
            self.show_message("\nPlease Enter a Number between 1 and 7\n", "bold yellow")
            return
        
    def show_message(self, massage, style):
            print(f"[{style}]{massage}[/{style}]")
        