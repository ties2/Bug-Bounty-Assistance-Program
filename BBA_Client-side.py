def testing_for_DOM_Based_Cross_Site_Scripting():
    print("testing_for_DOM_Based_Cross_Site_Scripting...")

def testing_for_JavaScript_Execution():
    print("testing_for_JavaScript_Execution...")

def testing_for_HTML_Injection():
    print("testing_for_HTML_Injection...")

def testing_for_Client_side_URL_Redirect():
    print("testing_for_Client_side_URL_Redirect...")

def testing_for_CSS_Injection():
    print("testing_for_CSS_Injection...")

def testing_for_Client_side_Resource_Manipulation():
    print("testing_for_Client_side_Resource_Manipulation...")

def testing_Cross_Origin_Resource_Sharing():
    print("testing_Cross_Origin_Resource_Sharing...")

def testing_for_Cross_Site_Flashing():
    print("testing_for_Cross_Site_Flashing...")

def testing_for_Clickjacking():
    print("testing_for_Clickjacking...")

def testing_WebSockets():
    print("testing_WebSockets...")

def testing_Web_Messaging():
    print("testing_Web_Messaging...")

def testing_Browser_Storage():
    print("testing_Browser_Storage...")

def testing_for_Cross_Site_Script_Inclusion():
    print("testing_for_Cross_Site_Script_Inclusion...")

process_steps = {
    '1': testing_for_DOM_Based_Cross_Site_Scripting,
    '2': testing_for_JavaScript_Execution,
    '3': testing_for_HTML_Injection,
    '4': testing_for_Client_side_URL_Redirect,
    '5': testing_for_CSS_Injection,
    '6': testing_for_Client_side_Resource_Manipulation,
    '7': testing_Cross_Origin_Resource_Sharing,
    '8': testing_for_Cross_Site_Flashing,
    '9': testing_for_Clickjacking,
    '10': testing_WebSockets,
    '11': testing_Web_Messaging,
    '12': testing_Browser_Storage,
    '13': testing_for_Cross_Site_Script_Inclusion,
}

while True:
    print("\nMain Menu:")
    print("1. Testing for DOM-Based Cross Site Scripting")
    print("2. Testing for JavaScript Execution")
    print("3. Testing for HTML Injection")
    print("4. Testing for Client-side URL Redirect")
    print("5. Testing for CSS Injection")
    print("6. Testing for Client-side Resource Manipulation")
    print("7. Testing Cross Origin Resource Sharing")
    print("8. Testing for Cross Site Flashing")
    print("9. Testing for Clickjacking")
    print("10. Testing WebSockets")
    print("11. Testing Web Messaging")
    print("12. Testing Browser Storage")
    print("13. Testing for Cross Site Script Inclusion")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")