'''Module which handles all database communication and data'''
from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from py_shared.hash.hashsalt import HashSalt

class UserDatabase():
    '''Class to handle database creation and communication'''
    def __init__(self, database_name: str) -> None:
        self.db = sqlite3.connect(database_name)
        self.connection = self.db.cursor()
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        salt VARCHAR(255) NOT NULL
        )
        """)

    def insert(self, user_data: UserData) -> None:
        '''Insert user information into the database'''
        data = (user_data.username, user_data.password, user_data.salt)
        self.connection.execute("INSERT INTO userdata (username, password, salt) VALUES (?, ?, ?)" , data)
        self.db.commit()

    def available_user(self, user_data: UserData) -> list:
        '''Get all database entries where username is the same and loop to find correct user'''
        self.connection.execute("SELECT * FROM userdata WHERE username = ?", (user_data.username,))
        for data in self.connection.fetchall():
            potential_password = HashSalt(user_data.password, data[3]).generate_salted_hash()
            if data[2] == potential_password:
                return data

@dataclass
class UserData():
    '''Dataclass to hold user information'''
    username: str
    password: str
    salt: bytes = None
