import pyperclip
class User:
    '''
        Create a new User with both Username and Password
    '''
    user_list = []
    @classmethod
    def __init__(self,username,passwordinfo):

        self.username = username        
        self.passwordinfo = passwordinfo

    def save_user(self):
        
        User.user_list.append(self)    

    def __init__(self, account_name, user_name, password_info):

        self.new_account = new_account
        self.user_name = Username
        self.passwordinfo = passwordinfo if passwordinfo else Accounts.password_new()

    
    def delete_user(self):
        '''
        delete_contact method deletes a saved account from the user_list
        '''
        User.user_list.remove(self)

    
    @classmethod
    def display_user(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list

class Accounts():
        '''
            This is a record of the account to be Created
        '''
    accounts_list = []

    @classmethod
    def contact_exist(cls,number):
        '''
        Checks if something is available 
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    def __init__(self, accountname, username, passwordinfo):
        '''
        Used to verify the account list
        '''
        self.accountname = accountname
        self.username = username
        self.passwordinfo = passwordinfo