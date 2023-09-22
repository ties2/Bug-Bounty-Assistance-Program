import docker


def Information_Gathering():
    print("Information Gathering process started...")


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

def Responsible_Disclosure():
    print("Responsible_Disclosure process started...")  


    #################################################################

def Communication():
    print("Communication process started...") 


    #################################################################

def Validation_and_Confirmation():
    print("Validation_and_Confirmation process started...") 


    #################################################################

def Validation_and_Confirmation():
    print("Validation_and_Confirmation process started...") 


    #################################################################

def Rewards_and_Acknowledgment():
    print("Rewards_and_Acknowledgment process started...") 


    #################################################################

def Continuous_Monitoring():
    print("Continuous_Monitoring process started...") 


    #################################################################

def Build_a_Portfolio():
    print("Build_a_Portfolio process started...") 


    #################################################################

def Learning_and_Skill_Enhancement():
    print("Build_a_Portfolio process started...") 


    #################################################################

def Network_and_Collaboration():
    print("Network_and_Collaboration process started...") 


    #################################################################

def Tools_and_Automation():
    
    print("Tools_and_Automation process started...") 

    def kali():
     print("kali process started...")
     client = docker.from_env()

     # Replace 'my_image' with the name of your Docker image
     client.containers.run('my_image', detach=True)
     print("Docker container started.")

    def Recon():
        print("Recon Tools...")
        
        

    Tools_Items = {
      '1': Recon,


     }

    while True:
     print("\n Tools menu:")
     print("1. Recon") 
     print("B. Back")

     tools_choice = input("Choose an option: ")
    
     if tools_choice in Tools_Items:
        Tools_Items[tools_choice]()
    
     elif tools_choice == 'E':
        break

     else:
        print("Invalid option, please try again.")


    #################################################################

def Ethical_Conduct_and_Compliance():
    print("Ethical_Conduct_and_Compliance process started...") 



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
    '8': Responsible_Disclosure,
    '9': Communication,
    '10': Validation_and_Confirmation,
    '11': Rewards_and_Acknowledgment,
    '12': Continuous_Monitoring,
    '13': Build_a_Portfolio,
    '14': Learning_and_Skill_Enhancement,
    '15': Network_and_Collaboration,
    '16': Tools_and_Automation,
    '17': Ethical_Conduct_and_Compliance,

    # Add the remaining process steps to this dictionary...
}

while True:
    print("\nMain Menu:")
    print("1. Information Gathering (Reconnaissance)")
    print("2. Scanning and Enumeration")
    print("3. Passive Scanning and Assessment")
    print("4. Active Scanning and Testing")
    print("5. Manual Testing")
    print("6. Exploit Development")
    print("7. Documentation and Reporting")
    print("8. Responsible Disclosure")
    print("9. Communication")
    print("10. Validation and Confirmation")
    print("11. Rewards and Acknowledgment")
    print("12. Continuous Monitoring")
    print("13. Build a Portfolio")
    print("14. Learning and Skill Enhancement")
    print("15. Network and Collaboration")
    print("16. Tools and Automation")
    print("17. Ethical Conduct and Compliance")
    print("18. Exit")


    main_choice = input("Choose an option: ")
    
    if main_choice in process_steps:
        process_steps[main_choice]()
    
    elif main_choice == '18':
        break

    else:
        print("Invalid option, please try again.")

           #################################################################
 

