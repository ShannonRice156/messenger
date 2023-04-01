'''Main module to be called from the command line. To start the server '''
from messenger.server import server

def main() -> None:
    '''main method to start the server'''
    server.main()

main()
