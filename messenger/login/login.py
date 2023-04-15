from enum import Enum, auto
from dataclasses import dataclass
from messenger.database.database import UserDatabase, UserData
from py_shared.hash.hashsalt import HashSalt

class LoginType(Enum):
    '''Enumeration which holds login tokens'''
    SUCCESSFUL = auto()
    FAILED = auto()
    INVALID_PASSWORD = auto()

@dataclass
class LoginToken():
    '''Represents a login token that contains user information and the type of login.'''
    type: LoginType
    data: UserData

class Account():
    '''Class that handles intialisation of database, users login and sign ups'''
    def __init__(self) -> None:
        self.database = None
    def login(self, data: UserData) -> LoginToken:
        '''Checks if the user is within the database and returns successful login if it us and failed if it isnt'''
        if self.user_database.available_user(data):
            return LoginToken(LoginType.SUCCESSFUL, data)
        else:
            return LoginToken(LoginType.FAILED, data)

    def signup(self, data: UserData) -> LoginToken:
        '''Encrypts the password given by the user data and inserts the user into the database'''
        encrpyt_password = HashSalt(data.password)
        hashed_data = encrpyt_password.generate_salted_hash()
        self.user_database.insert(UserData(data.username, hashed_data, encrpyt_password.salt))

    @property
    def user_database(self) -> UserDatabase:
        '''Instantiates the database when it is first called'''
        if getattr(self, "database") is None:
            self.database = UserDatabase()
        return self.database
