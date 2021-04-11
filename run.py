import random
from user import User
import unittest # Importing the unittest module
import pyperclip

def create_user(username,passwordinfo):
    '''
        Lets Create a New User
    '''
    user = User(username,passwordinfo)
    return(user)

        


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.username,"James")
    self.assertEqual(self.new_user.passwordinfo,"Muriuki")
    


if __name__ == '__main__':
    unittest.main()