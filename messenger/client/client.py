'''A module that creates the client side of the system'''
from py_shared.socket.sockets import SocketItem
from messenger.database.database import UserData
from py_shared.socket.socket_info import Info

class Client(SocketItem):
    ''' A class that handles the client socket connection and communication'''
    def __init__(self, socket_information: Info, data: UserData) -> None:
        super().__init__(socket_information)
        self.username = data.username

    def send_input(self, text: str):
        '''Awaits client input and sends message to super class to handle'''
        super().send(self.username + ": "+text)

    def connect_to_socket(self) -> None:
        '''Connects the client to the server socket'''
        self._socket.connect((self.info.host, self.info.port))

    def __eq__(self, __value: object) -> bool:
        return self.socket == __value.socket
