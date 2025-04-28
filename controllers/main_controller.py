from models.user import User
from models.menus import Menus
from controllers.data import Data

class MainController: 
    def __init__(self, view): 
        self.view = view
    