#BB assist project-Learning_and_sites
#BB assist project-Learning_and_sites
#BB assist project-Learning_and_sites
import webbrowser

def open_websites():
   def open_website(url):
       webbrowser.open(url, new=2)

   websites = {
       '1': {
           'name': 'awesome-bugbounty-tools',
           'url': 'https://github.com/vavkamil/awesome-bugbounty-tools'
       },
       '2': {
           'name': 'Shodan',
           'url': 'https://www.shodan.io'
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

if __name__ == "__main__":
   open_websites()
