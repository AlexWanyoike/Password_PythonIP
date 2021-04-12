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
    def user_exist(cls,username, passwordinfo):
        '''
        Checks if something is available 
        '''
        for user in User.user_list:
            if user.username == string:
                    return True

        return False

    def __init__(self, accountname, username, passwordinfo):
        '''
        Used to verify the account list
        '''
        self.accountname = accountname
        self.username = username
        self.passwordinfo = passwordinfo
    
    def save_details(self):
        '''
        Saving all the details
        '''

    def delete_accounts(self):
        '''
        Function to delete a contact
        '''
        Accounts.accounts_list.remove(self)

    @classmethod
    def find_accounts(cls, accountname):
        '''
        find all  the values 
        '''
        for accounts in cls.accounts_list:
            if accounts.accountname == accountname:
                return accounts

    

    chars = "qwertyuiopsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_="

    while 1:
        passwordinfo = int(input("What lengthe would you like:"))
        for x in range(0,1):
            password = ""
            for x in range(0,passwordinfo):
                password_char = random.choice(chars)
                password = password + password_char

            print("",password)

    