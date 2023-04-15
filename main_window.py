'''Main window to be called to start the main code and link UI and logic modules'''
#from messenger.client.client import Run
from PyQt5.QtWidgets import QApplication
from messenger.database.database import UserData
from messenger.login.login import Account, LoginType
from messenger.UI.login.main import Login
from messenger.UI.messenger.messenger_ui import Run as messenger_run
from messenger.client.client import Client, Info

def __login(main_app: QApplication) -> UserData:
    '''Method to instantiate and pass callables into the login UI class'''
    Login(main_app, __log_in, Account().signup)

def __log_in(main_app: QApplication, data: UserData) -> None:
    '''Checks if login is successful and proceeds to messenger screen if it is'''
    token = Account().login(data)
    if token is not None:
        if token.type == LoginType.SUCCESSFUL:
            sender = Client(Info())
            messenger_run(main_app, sender.send_input)


def main_loop() -> None:
    '''main method to run the client code'''
    main_app = QApplication([])
    __login(main_app)
    main_app.exec_()
