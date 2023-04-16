from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from messenger.database.database import UserData
from messenger.login.login import LoginToken

class Login(QMainWindow):
    '''Class to handle the display of the UI elements and their interactions'''
    def __init__(self, app: QApplication, login: callable, signup: callable) -> None:
        super(Login, self).__init__()
        uic.loadUi("ui_files/login.ui", self)
        self.check_login = login
        self.add_account = signup
        app.activeWindow = self
        self.app = app
        self.show()
        self.pushButton_3.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.signup)

    def login(self) -> LoginToken:
        return self.check_login(self.app, UserData(self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()))

    def signup(self) -> None:
        self.add_account(UserData(self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()))