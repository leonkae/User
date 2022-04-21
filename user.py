
import pyperclip

class User:
    '''  array to save user data'''
    
    user_list = []
    def __init__(self, first_name,last_name,email):
        
        
      ''' save new user data'''
      
    def save_user (self):
         User.user_list.append(self)
         
    @classmethod
    def email_exists(cls,email):
      for user in cls.user_list:
        if user.email == email:
              return True
        return False
      
    @classmethod
    def find_by_email (cls, email):
          for user in cls.user_list:
                if user.email == email:
                      return user.email
            
            
    @classmethod 
    def copy_email(cls,email):
      email_found = User.find_by_email(email)
      pyperclip.copy(email_found)
      
      

  