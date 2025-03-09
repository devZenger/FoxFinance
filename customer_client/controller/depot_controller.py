import sys
from view import DisplayMenuOption

from .depot_start_menu import DepotStartMenu
from .depot_stock_search import DepotStockSearch
from .depot_informationen import DepotInformation


class DepotControl:
    def __init__(self, token):
        self.token = token
        self.headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        self.option ={"1. Depot Übersicht": "depot overview",
                      "2. Aktien suche":"stock_search",
                      "3. Aktien kaufen": "buy stocks",
                      "4. Aktien verkaufen":"sell stocks",
                      "5. Informationen": "information",
                      "6. Abmelden":"loggout",
                      "7. Abmelden und benden":"loggout_and_exit"}
        
    def run(self):
        
        choice = "start"
        
        while True:
            
            match choice:
                    
                case "start":
                    depot_menu_start = DepotStartMenu(self.token, self.option)
                    choice = depot_menu_start.run()
                
                case "depot overview":
                    title ="Depot"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                case "stock_search":
                    stock_search = DepotStockSearch(self.token)
                    choice = stock_search.run()
                
                    
                case "buy stocks":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                
                case "sell stocks":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                case "information":
                    information = DepotInformation(self.token)
                    information.run()
                    choice = "start"
                    
                
                
                case "loggout":
                    del self.token
                    if isinstance(depot_menu_start, DisplayMenuOption):
                        del display_menu
                    
                    return
                
                case "loggout_and_exit":
                    del self.token
                    if isinstance(depot_menu_start, DisplayMenuOption):
                        del display_menu
                    
                    sys.exit(0)
                    
                    