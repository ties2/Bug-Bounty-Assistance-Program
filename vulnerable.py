#BB assist-vulnerable


def vulnerability():
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
        for i, vulnerability_name in enumerate(vulnerabilities.keys(), start=1):
            print(f"{i}. {vulnerability_name}")
        
        # Ask the user to choose a vulnerability
        choice = int(input("Enter the number of a vulnerability to run, or 0 to exit: "))
        
        # Exit the loop if the user chooses 0
        if choice == 0:
            break
        
        # Get the chosen vulnerability
        vulnerability_name = list(vulnerabilities.keys())[choice-1]
        
        # Run the chosen vulnerability
        print("Running {vulnerability_name}...")
        vulnerabilities[vulnerability_name]() 