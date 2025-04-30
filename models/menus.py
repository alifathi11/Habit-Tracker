from views.redirecting_animation import RedirectingAnimation

class Menus: 
    
    current_menu = None
    signup_menu = None
    login_menu = None
    main_menu = None
    exit_menu = None

    def __init__(self, signup_menu):
        super().__init__()

    @staticmethod
    def switch_menu(master, menu):

        if menu.lower() == "signup menu" and (master == Menus.login_menu or master == Menus.signup_menu):
            RedirectingAnimation.redirecting_animation("Redirecting to Signup Menu")
            Menus.current_menu = Menus.signup_menu
        elif menu == "login menu" and (master == Menus.login_menu or master == Menus.signup_menu):
            RedirectingAnimation.redirecting_animation("Redirecting to Login Menu")
            Menus.current_menu = Menus.login_menu
        elif menu == "main menu" and (master == Menus.login_menu): 
            RedirectingAnimation.redirecting_animation("Redirecting to Main Menu")
            Menus.current_menu = Menus.main_menu
        else:
            master.show_message("Invalid Menu Name.", "bold red")
            return