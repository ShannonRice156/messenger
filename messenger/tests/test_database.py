import random
import string
from py_shared.hash.hashsalt import HashSalt
from ..database import database

def test_database() -> None:
    '''Testing functionality of database class'''
    for i in range(10):
        test_str = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(8)))
        hash_obj = HashSalt(test_str)
        hashed_data = hash_obj.generate_salted_hash()
        name = ''.join(random.choice(string.ascii_letters) for i in range(8))
        data = database.UserData(name, hashed_data, hash_obj.salt)
        db = database.UserDatabase("userdata.db")
        db.insert(data)

        sign_in_user = database.UserData(name, test_str)
        retrieved_data = db.available_user(sign_in_user)
        assert retrieved_data[1] == name
        assert retrieved_data[2] == hashed_data
        assert retrieved_data[3] == hash_obj.salt
