'''A module that creates the client side of the system'''
from py_shared.socket.sockets import SocketItem

class Client(SocketItem):
    ''' A class that handles the client socket connection and communication'''
    def send_input(self, text: str):
        '''Awaits client input and sends message to super class to handle'''
        super().send(text)

    def connect_to_socket(self) -> None:
        '''Connects the client to the server socket'''
        self._socket.connect((self.info.host, self.info.port))

    def __eq__(self, __value: object) -> bool:
        return self.socket == __value.socket
