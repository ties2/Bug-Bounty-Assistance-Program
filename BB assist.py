import docker
import sys
from PIL import Image
from termcolor import colored
from ascii_magic import AsciiArt

##########image of start###############
print("welcome to BB Assist")
my_art = AsciiArt.from_image('/Volumes/myjob/Computer/Programming/Projects/python/BB assist/BB assist copy.png')
my_art.to_terminal()
    #################################################################

def Information_Gathering():
    print("Information Gathering process started...")
    #Recon
    def print_checklist(checklist):
     for i, (item, checked) in enumerate(checklist.items(), start=1):
        status = "[x]" if checked else "[ ]"
        print(f"{i}. {status} {item}")

     def toggle_item(checklist, item_number):
       item = list(checklist.keys())[item_number-1]
       checklist[item] = not checklist[item]

     checklist = {
       "Item 1": False,
       "Item 2": False,
       "Item 3": False,
    # Add more items...
     }

     while True:
      print_checklist(checklist)
      item_number = int(input("Enter item number to check/uncheck, or 0 to exit: "))
    
      if item_number == 0:
        break
      elif 1 <= item_number <= len(checklist):
        toggle_item(checklist, item_number)
      else:
        print("Invalid item number, please try again.")





    #################################################################

def Scanning_and_Enumeration():
    print("Scanning and Enumeration process started...")

    #################################################################
    

def Passive_Scanning_and_Assessment():
    print("Passive_Scanning_and_Assessment process started...")


    #################################################################

def Active_Scanning_and_Testing():
    print("Active_Scanning_and_Testing process started...")



    #################################################################

def Manual_Testing():
    print("Manual_Testing process started...")


    #################################################################

def Exploit_Development():
    print("Exploit_Development process started...")


    #################################################################

def Documentation_and_Reporting():
    print("Documentation_and_Reporting process started...")


    #################################################################

def Communication():
    print("Communication process started...") 


    #################################################################

def Validation_and_Confirmation():
    print("Validation_and_Confirmation process started...") 


    #################################################################

def Continuous_Monitoring():
    print("Continuous_Monitoring process started...") 


    #################################################################

def Build_a_Portfolio():
    print("Build_a_Portfolio process started...") 


    #################################################################

def Learning_and_sites():
    print("Build_a_Portfolio process started...") 
#some sites for refrences

    import webbrowser

    def open_website(url):
     webbrowser.open(url, new=2)

    websites = {
      '1': {
        'name': 'awesome-bugbounty-tools',
        'url': 'https://github.com/vavkamil/awesome-bugbounty-tools'
      },
      '2': {
        'name': 'Shodan',
        'url':  'https://www.shodan.io'
      },
      '3': {
        'name': 'eyezoome',
        'url': 'https://www.zoomeye.org'
     },
      '4': {
        'name': 'Censys',
        'url': 'https://censys.com'
     },
      '5': {
        'name': 'ypugetsignal',
        'url': 'https://www.yougetsignal.com'
     },
      '6': {
        'name': 'virustotal',
        'url': 'https://www.virustotal.com/gui/home/upload'
    },
      'E': {
        'name': 'Exit',
        'url': ''
      }

    }

    while True:
     print("\nWebsites Menu:")
     for key, site in websites.items():
        print(f"{key}. {site['name']}")
        
     choice = input("Choose a website to open: ")

     if choice in websites:
         if choice == 'E':
            break
         open_website(websites[choice]['url'])
    
     else:
        print("Invalid option, please try again.")





    #################################################################

def Network_and_Collaboration():
    print("Network_and_Collaboration process started...") 


    #################################################################

def Tools():
    
    print("Tools_and_Automation process started...") 
    #use image docker custome
    def kali():
     print("kali process started...")
     client = docker.from_env()

     # Replace 'my_image' with the name of your Docker image
     client.containers.run('my_image', detach=True)
     print("Docker container started.")

    def Recon():
        print("Recon Tools...")
        
        

    Tools_Items = {
      '1': kali,
    


     }

    while True:
     print("\n Tools menu:")
     print("1. Recon") 
     print("B. Back")

     tools_choice = input("Choose an option: ")
    
     if tools_choice in Tools_Items:
        Tools_Items[tools_choice]()
    
     elif tools_choice == 'B':
        break

     else:
        print("Invalid option, please try again.")


    #################################################################

def Ethical_Conduct_and_Compliance():
    print("Ethical_Conduct_and_Compliance process started...") 

       #################################################################
 
def Vulnerabilities():
    print("Ethical_Conduct_and_Compliance process started...") 

    # Define your functions
    #Server-side-attack
    def SQL_Injection():
        pass  # Add your code here

    def Authentication():
        pass  # Add your code here

    def Directory_Traversal():
        pass  # Add your code here 

    def Command_Injection():
        pass  # Add your code here

    def Business_logic_vulnerabilities():
        pass  # Add your code here

    def Inforamtion_Disclosure():
        pass  # Add your code here

    def Access_Control():
        pass  # Add your code here

    def File_upload_vulnerabilities():
        pass  # Add your code here

    def Race_conditions():
        pass  # Add your code here

    def SSRF():
        pass  # Add your code here

    def XXE(): 
        pass  # Add your code here

        #Client-side attacks

    def XSS():
        pass  # Add your code here


    def CSRF():
       pass  # Add your code here 

    def ClickJacking():
       pass  # Add your code here
    def DomBased():
       pass  # Add your code here

    def CORS():
       pass  # Add your code here

    def WebSockets():
       pass  # Add your code here

    #Advanced

    def Http_Request_Smuggling():
       pass  # Add your code here

    def Serversidetemplate_injection():
       pass  # Add your code here

    def Insecure_deserialization():
       pass  # Add your code here

    def OAuth_Authentication():
       pass  # Add your code here

    def web_cache_poisoning():
       pass  # Add your code here

    def HTTP_host_header_attacks():
       pass  # Add your code here

    def JWT_attacks():
        pass  # Add your code here

    def Prototype_Pollution():
        pass  # Add your code here

    def GraphQL_API_vulnerabilities():
        pass  # Add your code here

    
     # Create a dictionary to map vulnerability names to functions
    vulnerabilities = {
        "SQL Injection": SQL_Injection,
        "Authentication": Authentication,
        "Directory_Traversal":Directory_Traversal,
        "Command_Injection":Command_Injection,
        "Business_logic_vulnerabilities":Business_logic_vulnerabilities,
        "Inforamtion_Disclosure":Inforamtion_Disclosure,
        "Access_Control":Access_Control,
        "File_upload_vulnerabilities":File_upload_vulnerabilities,
        "Race_conditions":Race_conditions,
        "SSRF":SSRF,
        "XXE":XXE,
        "XSS":XSS,
        "CSRF":CSRF,
        "ClickJacking":ClickJacking,
        "DomBased":DomBased,
        "CORS":CORS,
        "WebSockets":WebSockets,
        "Http_Request_Smuggling":Http_Request_Smuggling,
        "Serversidetemplate_injection":Serversidetemplate_injection,
        "Insecure_deserialization":Insecure_deserialization,
        "OAuth_Authentication":OAuth_Authentication,
        "web_cache_poisoning":web_cache_poisoning,
        "HTTP_host_header_attacks":HTTP_host_header_attacks,
        "JWT_attacks":JWT_attacks,
        "Prototype_Pollution":Prototype_Pollution,
        "GraphQL_API_vulnerabilities":GraphQL_API_vulnerabilities,
        # Add the rest of your vulnerabilities here...
    } 

    while True:
        # Print the menu
        for i, vulnerability in enumerate(vulnerabilities, start=1):
            print(f"{i}. {vulnerability}")
        
        # Ask the user to choose a vulnerability
        choice = int(input("Enter the number of a vulnerability to run, or 0 to exit: "))
        
        # Exit the loop if the user chooses 0
        if choice == 0:
            break
        
        # Get the chosen vulnerability
        vulnerability = list(vulnerabilities.values())[choice-1]
        
        # Run the chosen vulnerability
        vulnerability()

       #################################################################


# Add the remaining process steps in a similar way...

# Create a dictionary of process steps
process_steps = {
    '1': Information_Gathering,
    '2': Scanning_and_Enumeration,
    '3': Passive_Scanning_and_Assessment,
    '4': Active_Scanning_and_Testing,
    '5': Manual_Testing,
    '6': Exploit_Development,
    '7': Documentation_and_Reporting,
    '12': Continuous_Monitoring,
    '13': Build_a_Portfolio,
    '14': Learning_and_sites,
    '15': Network_and_Collaboration,
    '16': Tools,
    '17': Ethical_Conduct_and_Compliance,
    '18': Vulnerabilities,

    # Add the remaining process steps to this dictionary...
}

while True:
    print("\nMain Menu:")
    print("1. Information Gathering")
    print("2. Scanning and Enumeration")
    print("3. Passive Scanning and Assessment")
    print("4. Active Scanning and Testing")
    print("5. Manual Testing")
    print("6. Exploit Development")
    print("7. Documentation and Reporting")
    print("12. Continuous Monitoring")
    print("13. Build a Portfolio")
    print("14. Learning and Sites")
    print("15. Network and Collaboration")
    print("16. Tools")
    print("17. Ethical Conduct and Compliance")
    print("18. vulnerabities")
    print("E. Exit")


    main_choice = input("Choose an option: ")
    
    if main_choice in process_steps:
        process_steps[main_choice]()
    
    elif main_choice == 'E':
        break

    else:
        print("Invalid option, please try again.")

           #################################################################
 



