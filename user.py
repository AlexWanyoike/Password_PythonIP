import pyperclip
class User:
    '''
        Create a new User with both Username and Password
    '''
    user_list = []

    def __init__(self,username,passwordinfo):

        self.username = username        
        self.passwordinfo = passwordinfo

    def save_user(self):
        
        User.user_list.append(self)    
    
    def delete_user(self):
        '''
        delete_contact method deletes a saved account from the user_list
        '''
        User.user_list.remove(self)