#BB assist project 
#here we check steps of Recon 
#1.find sunbdomains


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
}
while True:
      print("\nRecon tools:")
      print("1. subfinder")
      print("2. dnsx")
      print("3. httpx")
      print("4. nnuclei")
      print("5. Gowitness")
      print("6. ffuf")
      print("E. Exit")

      option = input("Enter an option: ").strip()

      if option == 'E' or option == 'e':
            break

      if option in process_steps:
            print(process_steps[option].__name__)
            process_steps[option]()
      else:
            print("Invalid option. Please try again.")







