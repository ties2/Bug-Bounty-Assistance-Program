#BB assist project 
#here we check steps of Recon 
#1.find sunbdomains



def ReconBB():
   def subfinder():
    print("Running subfinder...")

   def dnsx():
    print("Running dnsx...")

   def httpx():
    print("Running httpx...")

   def Gowitness():
    print("Running Gowitness...")

   def ffuf():
    print("Running ffuf...")

   def nuclei():
    print("Running nuclei...")

   process_steps = {
    '1': subfinder,
    '2': dnsx,
    '3': httpx,
    '4': Gowitness,
    '5': ffuf,
    '6': nuclei,
    


    # Add the remaining process steps to this dictionary...
 }
   
   while True:
      print("\nMain Menu:")
      print("1. subfinder")
      print("2. dnsx")
      print("3. httpx")
      print("4. nnuclei")
      print("5. Gowitness")
      print("6. ffuf")
      print("E. Exit")
      
      main_choice = input("Choose an option: ")
      
      if main_choice in process_steps:
         process_steps[main_choice]()
      
      elif main_choice == 'E':
         break

      else:
         print("Invalid option, please try again.")
 
 
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






