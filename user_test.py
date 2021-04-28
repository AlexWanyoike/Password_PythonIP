import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    '''
    This test defines user class behavior
    '''

    def setUp(self):
        self.new_user = User("Moringa", "password")
    
    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Moringa")
        self.assertEqual(self.new_user.password, "password")
    
    '''
    test 2 : test if a new user can be added
    '''

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    '''
    test 3 : Use teardown method which helps in cleaning up code
    '''

    def tearDown(self):
        User.user_list = []
    '''
    test for saving multi-users
    '''

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Moringa", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    '''
    test 4 : Deleting a user
    '''

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Moringa", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
    
    '''
    test 5 : find user by first name and display info
    '''

    def test_find_user_by_user_name(self):
        self.new_user.save_user()
        test_user = User("Moringa", "password")
        test_user.save_user()
        found_user = User.find_by_user_name("Moringa")
        self.assertEqual(found_user.user_name,test_user.user_name)

    '''
    test 6 : if a user exists return a boolean
    '''

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Moringa", "password")
        test_user.save_user()
        user_exists = User.user_exist("Moringa")
        self.assertTrue(user_exists)

    '''
    test 7 : display list of all users saved
    '''

    def test_display_all_users(self):
        self.assertEqual(User.display_users(), User.user_list)


if __name__ == '__main__':
    unittest.main()