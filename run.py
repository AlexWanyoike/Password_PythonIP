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

def find_accounts(numbers):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Accounts.find_accounts(number)

def password_new():
    '''
        Password generator
    '''
    new_pass = Accounts.password_new()
    return new_pass

def display_user_details():
    '''
    Display all User Details
    '''
    return Accounts.display_accounts()

def main():
    while True:
        print('\n')
        print("This is the lastest Password Input Locker")
        print("Use these short codes : cc - create a new user, dc - display user, fc -find accounts, ex -exit the contact list ")

        short_code = input().lower()
        print('\n')
        if short_code == 'cc'
            username = input()

            while True:
                print("Create a New Username")
                username = input()
                while True:
                    print("Would you like to create your own Password or generated?")
                    passwordint = input().lower().strip()
                    if passwordint === 'own'
                        passwordint = input(Enter own Password)
                    
                    else passwordint === 'generate'
                        passwordint = password()

                    save_user(create_user(accountname,username,passwordinfo))
                    print ('\n')
                    print(f"New User{accountname} {username} {passwordinfo} created")
                    print ('\n')

         elif short_code == 'dc':

                    if display_user():
                            print("Here is a list of all your users")
                            print('\n')
                        for accounts in display_user_details():
                            print(f"User {accountname}  Password {passwordinfo}")

        
                            
                    




if __name__ == '__main__':
    unittest.main()



    


