import sys

from view import Display

from .main_create_account import CreateAccountMenu
from .main_login import LoginMenu
from .depot_controller import DepotControl
from .informationen import AllInformation


class MainControl:
    def __init__(self):
        self.title = "Hauptmenü"
        self.options = {"1. Login": "login",
                        "2. Konto erstellen": "create_account",
                        "3. Beispiel Depot testen": "example_account",
                        "4. Informationen": "information",
                        "5. Beenden": "exit"}

    def run(self):

        display = Display()

        choice = "welcome"

        while True:

            match choice:
                case "welcome":
                    display.display_title(self.title)
                    info = "Willkommen bei Fox Finance"
                    display.display_info(info)
                    choice = display.display_options(self.options)

                case "start":
                    display.display_title(self.title)
                    choice = display.display_options(self.options)

                case "create_account":
                    create_account = CreateAccountMenu()
                    choice = create_account.run()

                case "login":
                    login_menu = LoginMenu()
                    success, token = login_menu.run()
                    if success:
                        depot_controller = DepotControl()
                        depot_controller.run(token)

                        del depot_controller
                        del token

                    choice = "start"

                case "example_account":
                    example_login = LoginMenu()
                    success, token = example_login.start_example_account()
                    if success:
                        depot_controller = DepotControl()
                        depot_controller.run(token)

                        del depot_controller
                        del token
                    else:
                        display.display_info(token)
                    choice = "start"

                case "information":
                    information = AllInformation(self.options)
                    choice = information.run()

                case "exit":
                    sys.exit(0)
