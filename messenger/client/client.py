'''A module that creates the client side of the system'''
import threading
from py_shared.socket.sockets import SocketItem
from py_shared.socket.socket_info import Info

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

def Run() -> None:
    '''Main server method to start client connection'''
    sender = Client(Info())
    thread2 = threading.Thread(target=sender.send_input)
    thread2.start()

    while True:
        print(sender.receive())
