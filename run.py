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

def main():
    print("")

            while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    unittest.main()



    


