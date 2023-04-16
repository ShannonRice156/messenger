'''Module to handle all basic UI functionality for QmainWindow that would be otherwise duplicated'''
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Base(QMainWindow):
    '''Base class for all ui that instantiates variables and loads ui file'''
    def __init__(self, app: QApplication, file_name: str) -> None:
        super(Base, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui_files/"+ file_name), self)
        app.activeWindow = self
        self.app = app
        self.show()
