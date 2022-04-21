import email
from operator import length_hint
import unittest


from pytest import TestReport
from user import User

import pyperclip

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User("jane","Doe","none@gmail.com")
        
    def test_init(self):
        self.assertEqual(self.new_user.f_name,"jane")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.email,"none@gmail.com")
        
    def tearDown(self):
        User.user_list =[]
        
    def test_save(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_users(self):
        self.new_user.save_user()
        extra_user =User("John","Doe","extrauser@gmail.com")
        extra_user.save_user()
        self.assertEqual(len(User.user_lists),2)
        
    def test_email_exists(self):
        self.new_user.save_user()    
        new_user = ("Jane", "Doe","none@gmail.com")
        new_user.save_user()
        email_exists = User.email_exists("none@gmail.com")
        self.assertTrue(email_exists)
        
    def test_copy_email(self):
        self.new_user.save_user()
        User.copy_email("none@gmail.com")
        self.assertEqual(self.new_user.email, pyperclip.paste)
        
        
        

if __name__=='__main__':
    unittest.main()                
                
        