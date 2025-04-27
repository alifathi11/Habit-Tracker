class Menus: 
    
    current_menu = None
    register_menu = None
    login_menu = None
    exit_menu = None

    def __init__(self, register_menu):
        super().__init__()
        Menus.current_menu = register_menu


    @staticmethod
    def menu_switcher(self, menu):
        if menu == self.register_menu: 
            pass
        elif menu == self.login_menu:
            pass
        #TODO

        
