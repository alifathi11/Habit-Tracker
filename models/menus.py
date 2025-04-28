class Menus: 
    
    current_menu = None
    signup_menu = None
    login_menu = None
    exit_menu = None

    def __init__(self, signup_menu):
        super().__init__()

    @staticmethod
    def switch_menu(master, menu):

        if menu.lower() == "signup menu" and (master == Menus.login_menu or master == Menus.signup_menu):
            master.show_massage("Redirecting to Signup Menu...")
            Menus.current_menu = Menus.signup_menu
        elif menu == "login menu" and (master == Menus.login_menu or master == Menus.signup_menu):
            master.show_massage("Redirecting to Login Menu...")
            Menus.current_menu = Menus.login_menu
        else:
            master.show_massage("Invalid Menu Name.")