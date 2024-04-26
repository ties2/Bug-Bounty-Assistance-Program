#BB assist-Tools
import docker

def Tool():
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
