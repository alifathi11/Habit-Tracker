class RegisterView(): 
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def handle_input(self):

        input_command = input()

        if input_command.lower() == "register":

            username = input("Please Enter Your Username: ")
            password = input("Please Enter Your Password: ")
            email = input("Please Enter Your Email Address: ")
            
            self.controller.register(username, password, email)

        else:
            self.show_massage("Invalid command.")

    def show_massage(self, massage):
            print(massage)