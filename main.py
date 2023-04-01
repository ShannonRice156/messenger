'''Main module to be called from the command line to invoke the client code'''
from messenger.client import client

def main() -> None:
    '''main method to run the client code'''
    client.main()

main()
