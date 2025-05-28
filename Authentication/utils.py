import os

def get_password_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    passwords_path = os.path.join(parent_dir, 'wordlists', 'passwords.txt')
    with open(passwords_path, 'r') as f:
        return f.read().splitlines()
    
def get_username_wordlist() -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    users_path = os.path.join(parent_dir, 'wordlists', 'users.txt')
    with open(users_path, 'r') as f:
        return f.read().splitlines()