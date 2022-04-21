#!/usr/bin/env python3.9

from user import User



def create_user(f_name, l_name, email):
    new_user =  User(f_name,l_name, email)
    return new_user

def save_user(user):
    user.save_user()
    
def find_email(email):
    return User.find_by_email(email)

def main():
    print("hello user, welcome to our to appliction, whats your name?")
    user_name = input()
    print(f"hello {user_name}, what would you like to do")
    print('\n')
    while True:
        print("use this short codes: cu-createuser, fe- findemail, ex - exit on the application")
        short_code = input().lower()
        if short_code =='cu':
            print("New User")
            print("First Name")
            f_name = input()
            
            print("Last Name")
            l_name = input ()
            
            print("Email")
            email = input()
            
            save_user(create_user(f_name,l_name,email))
            print('\n')
            # print(f'New User {f_name} {l_name} {email} has been created')
            
        elif short_code == 'ex':
            print("Bye hope to see you soon")  
            break  
        else:
            print(" Invalid Input please use the shortcodes provided")
              
            
            
            
    
if __name__ == '__main__':
    main()


    
    