import requests
from termcolor import colored

#Techonology class
class Technology:
    '''Class describing technology like Wordpress or Django. Gets name of technology and default path to admin panel'''
    def __init__(self, name: str, path: str) -> None:
        super().__init__()
        self.name = name
        self.path = path
        #Is this path exist on site
        self.avalaible = False
    
    def checkPath(self, website):
        '''Checks if panel exist by sending HTTP GET request'''
        URL = 'http://' + website + self.path
        req = requests.get(URL)
        status_code = req.status_code

        #If status code is between 200 and 300 page exists
        if status_code >= 200 and status_code < 300:
            print(colored(f"Possible {self.name} panel: {URL} exists", 'green'))
        #If status code is between 300 and 400 page probably exists but there's a redirection message
        elif status_code >= 300 and status_code < 400:
            print(colored(f"Possible {self.name} panel: {URL} has {status_code} response code", 'blue'))
        #If status code is between 400 and 500 page doesn't exist or you need authenticate yourself 
        elif status_code >= 400 and status_code < 500:
            print(colored(f"{URL} doesn't exist. {status_code} code", 'red'))
        else:
        #Other like 1xx codes or 5xx
            print(colored(f"{status_code} code", 'blue'))

#You can add your own technologies to this list
technologies = [Technology("Wordpress", "/wp-admin"), Technology("Joomla", "/administrator"), Technology("Django", "/admin"), Technology("PHPmyadmin", "/phpmyadmin")]


#ASCII ART
print("    _       _           _         ____                  _")
print("   / \   __| |_ __ ___ (_)_ __   |  _ \ __ _ _ __   ___| |")
print("  / _ \ / _` | '_ ` _ \| | '_ \  | |_) / _` | '_ \ / _ \ |")
print(" / ___ \ (_| | | | | | | | | | | |  __/ (_| | | | |  __/ |")
print("/_/   \_\__,_|_| |_| |_|_|_| |_| |_|   \__,_|_| |_|\___|_|")
print(" ____                      _")
print("/ ___|  ___  __ _ _ __ ___| |__   ___ _ __")
print("\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|")
print(" ___) |  __/ (_| | | | (__| | | |  __/ |")
print("|____/ \___|\__,_|_|  \___|_| |_|\___|_|")
print("")

print("This tool may be quite slow")
print("Type website address: ", end='')
website = input()

for tech in technologies:
    tech.checkPath(website)
print("Thanks for using Admin Panel Searcher")