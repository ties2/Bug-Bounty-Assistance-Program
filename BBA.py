import docker
import sys
#import mysql.connector
import webbrowser
from PIL import Image
from termcolor import colored
#from ascii_magic import AsciiArt
from Learning_and_sites import open_websites
from Tools import Tool
from vulnerable import vulnerability
from BBA_WSTGinfo import WSTG_info
from BBA_Report import Report


##########image of start###############
print("welcome to BB Assist")
# my_art = AsciiArt.from_image('/Volumes/myjob/Computer/Programming/Projects/python/BB assist/BB assist copy.png')
# clearmy_art.to_terminal()
    #################################################################
def WSTG_info():
    print("Recon...")
    
    #Information_Gathering()

    #################################################################


def Exploit_Development():
    print("Exploit_Development process started...")


    #################################################################

def Documentation_and_Reporting():
    print("Documentation_and_Reporting process started...")
    #reporting
    Report()

    #################################################################

def Build_a_Portfolio():
    print("Build_a_Portfolio process started...") 


    #################################################################

def Learning_and_sites(url):
    print("learning_and_sites...")
    open_websites()

    #################################################################

def Vulnerabilities():
    print("Ethical_Conduct_and_Compliance process started...") 

    # Define your functions
    #Server-side-attack
    def SQL_Injection():
        pass  # Add your code here


    #################################################################
def Tools():
    
    print("Tools_and_Automation process started...") 
    Tool()

    #################################################################

def Vulnerabilities():
    print("Ethical_Conduct_and_Compliance process started...") 
    vulnerability()


#################################################################
    


def Web_app_Checklist():
    print("web_app_checklist process started...") 

#################################################################

# Add the remaining process steps in a similar way...
def main():
    print("test")
# Create a dictionary of process steps
process_steps = {
        '1': WSTG_info,
        '2': Exploit_Development,
        '3': Documentation_and_Reporting,
        '4': Build_a_Portfolio,
        '5': Learning_and_sites,
        '7': Tools,
        '8': Vulnerabilities,
        '9': Web_app_Checklist,
        

        # Add the remaining process steps to this dictionary...
    }

while True:
        print("\nMain Menu:")
        print("1. Recon")
        print("2. Exploit Development")
        print("3. Documentation and Reporting")
        print("4. Build a Portfolio")
        print("5. Learning and Sites")
        print("7. Tools")
        print("8. vulnerabities")
        print("9. Web app Checklist")
        print("E. Exit")


        main_choice = input("Choose an option: ")
        
        if main_choice in process_steps:
            process_steps[main_choice]()
        
        elif main_choice == 'E':
            break

        else:
            print("Invalid option, please try again.")
main()
            
    
