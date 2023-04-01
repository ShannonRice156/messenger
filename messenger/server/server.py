'''A module that creates the server side of the system'''
import threading
from py_shared.socket.sockets import SocketItem
from py_shared.socket.socket_info import Info
from ..client.client import Client

class MessageServer(SocketItem):
    ''' A class that handles the server socket connection and communication'''
    def __init__(self, server_info: Info) -> None:
        self._clients = []
        super().__init__(server_info)

    def update(self, message: str, sender: Client) -> None:
        '''Updates other clients connected to the server with the message sent from a user'''
        for client in self._clients:
            if sender != client:
                try:
                    client.send(message)

                except:
                    self._clients.remove(client)

    def connect_to_socket(self) -> None:
        '''Binds the server to the host and port given'''
        self._socket.bind((self.info.host, self.info.port))

    def check_messages(self, new_client: Client) -> None:
        '''Reoccuring loop to check if a message has been sent by a client'''
        while True:
            message = new_client.receive()
            new_client.send('Received')
            self.update(message, new_client)

    def poll(self):
        '''Reoccuring loop to accept any new client connections 
           and generate their own threads to check for messages'''
        while True:
            new_socket = self.socket.accept()
            new_client = Client(Info())
            new_client.send('Connected')
            new_client.socket = new_socket
            self._clients.append(new_client)
            thread = threading.Thread(target=self.check_messages, args=(new_client,))
            thread.start()

def main() -> None:
    '''Main server method to start server if it is not already running'''
    messenger = MessageServer(Info())
    messenger.run()
    while True:
        messenger.poll()

if __name__ == "__main__":
    main()
