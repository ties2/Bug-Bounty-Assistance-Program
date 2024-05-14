
import requests
import os
import re

# Use an environment variable for the token to keep it secure
API_TOKEN = os.getenv('API_TOKEN')

if not API_TOKEN:
    raise ValueError("API_TOKEN environment variable is not set")

url = "https://api.example.com/endpoint"

# Set headers including the Authorization header with the Bearer token
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
        print(response.json())
        
        # Test for vulnerabilities
        
        
        
        
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

def send_request(url, method='GET', headers=None, params=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def check_response(response):
    if response is None:
        return False
    if response.status_code!= 200:
        return False
    return True

def test_sql_injection(url):
    payload = "' OR '1'='1"
    params = {"id": payload}
    response = send_request(url, params=params)
    if "error" in response.text.lower() and check_response(response):
        print("Potential SQL injection vulnerability detected!")
    else:
        print("No SQL injection vulnerability found.")

def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    params = {"q": payload}
    response = send_request(url, params=params)
    if payload in response.text and check_response(response):
        print("Reflected XSS vulnerability detected!")
    else:
        print("No reflected XSS vulnerability found.")

def test_xx_e(url):
    payload = '<?xml version="1.0" encoding="UTF-8"?><DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><root>&xxe;</root>'
    headers = {"Content-Type": "application/xml"}
    response = send_request(url, headers=headers, data=payload)
    if "root:x" in response.text and check_response(response):
        print("XXE vulnerability detected!")
    else:
        print("No XXE vulnerability found.")




def testing_GraphQL():
    print("testing_GraphQL...")

def test_sql_injection(url):
    print("test_sql_injection...")


process_steps = {
    '1': testing_GraphQL,
    '2': test_sql_injection(url),
    '3': test_xss(url),
    '4': test_xx_e(url)
}

while True:
    print("\nMain Menu:")
    print("1. testing_GraphQL")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")