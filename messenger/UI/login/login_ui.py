'''Module to handle all Login UI classes and functions'''
from PyQt5.QtWidgets import QApplication
from ..base_ui import Base
from messenger.database.database import UserData
from messenger.login.login import LoginToken

class Login(Base):
    '''Class to handle the display of the UI elements and their interactions'''
    def __init__(self, app: QApplication, login: callable, signup: callable) -> None:
        super(Login, self).__init__(app, "login.ui")
        self.check_login = login
        self.add_account = signup
        self.pushButton_3.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.signup)

    def login(self) -> LoginToken:
        return self.check_login(self.app, UserData(self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()))

    def signup(self) -> None:
        self.add_account(UserData(self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()))
