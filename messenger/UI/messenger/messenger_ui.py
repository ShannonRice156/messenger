'''Module to handle all messenger UI classes and functions'''
from PyQt5.QtWidgets import QApplication
from ..base_ui import Base

class Messenger(Base):
    '''Class to handle the display of the UI elements and their interactions'''
    def __init__(self, app: QApplication, send: callable) -> None:
        '''Initialises UI elements and sets the callable send function to be callable within this class'''
        super(Messenger, self).__init__(app, "Messenger.ui")
        self.send = send
        self.pushButton.clicked.connect(self.send_pressed)

    def send_pressed(self) -> None:
        '''Retrieves text from the text edit UI element and passes it through to the send method'''
        self.send(self.inputbox.text())

    def message_recieved(self, message: str) -> None:
        '''Updates text box with message given and sets scrollbar to the maximum'''
        self.textEdit.append(message)
        self.textEdit.update()
        self.update_scrollbar()

    def update_scrollbar(self) -> None:
        '''Updates the scrollbar to the maximum position'''
        self.textEdit.verticalScrollBar().setValue(self.textEdit.verticalScrollBar().maximum()+20)
