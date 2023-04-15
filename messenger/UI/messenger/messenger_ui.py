'''Module to handle all messenger UI classes and functions'''
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Messenger(QMainWindow):
    def __init__(self, app: QApplication, send: callable) -> None:
        '''Initialises UI elements and sets the callable send function to be callable within this class'''
        super(Messenger, self).__init__()
        uic.loadUi("ui_files/Messenger.ui", self)
        super(Messenger, self).show()
        self.send = send
        self.app = app
        self.show()
        self.pushButton.clicked.connect(self.send_pressed)

    def send_pressed(self) -> None:
        '''Retrieves text from the second text edit UI element and passes it through to the send method'''
        self.send(self.textEdit_2.toPlainText())

def Run(app: QApplication, send: callable) -> None:
    '''Destroys the previous active window and sets the messenger class as the current one'''
    app.activeWindow.destroy()
    app.activeWindow = Messenger(app, send)
