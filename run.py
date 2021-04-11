import random
from user import User , Accounts
import pyperclip

def create_user(username,passwordinfo):
    '''
        Lets Create a New User
    '''
    user = User(username,passwordinfo)
    return(user)

def save_user(user):
    '''
    Function to save contact
    '''
    contact.save_user()

def create_newaccount(accountname, username, passwordinfo):
    '''
        Trying to create a new Account
    '''
    newaccount = Accounts(accountname,username,passwordinfo)
    return (newaccount)

def save_accounts(accounts):

    accounts.save_accounts()

def delete_accounts(accounts):
    '''
    Function to delete an account
    '''
    accounts.delete_accounts()



if __name__ == '__main__':
    unittest.main()



    


