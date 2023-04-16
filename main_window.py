'''Main window to be called to start the main code and link UI and logic modules'''
import threading
from PyQt5.QtWidgets import QApplication
from messenger.database.database import UserData
from messenger.login.login import Account, LoginType
from messenger.UI.login.main import Login
from messenger.UI.messenger.messenger_ui import Messenger
from messenger.client.client import Client
from py_shared.socket.socket_info import Info



def __login(main_app: QApplication) -> UserData:
    '''Method to instantiate and pass callables into the login UI class'''
    Login(main_app, __log_in, Account().signup)

def check_messages(messenger: Messenger, sender: Client):
    while True:
        message = sender.receive()
        messenger.message_recieved(message)
                
def __log_in(main_app: QApplication, data: UserData) -> None:
    '''Checks if login is successful and proceeds to messenger screen if it is'''
    token = Account().login(data)
    if token is not None:
        if token.type == LoginType.SUCCESSFUL:
            sender = Client(Info())
            messenger = Messenger(main_app, sender.send_input)
            thread = threading.Thread(target=check_messages, args=(messenger,sender))
            thread.daemon = True
            thread.start()

def main_loop() -> None:
    '''main method to run the client code'''
    main_app = QApplication([])
    thread = threading.Thread(target =__login, args=(main_app, ))
    thread.run()
    main_app.exec()
