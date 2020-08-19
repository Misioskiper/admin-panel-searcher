import requests

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

        if status_code >= 200 and status_code < 300:
            print(f"{URL} exists")
        elif status_code >= 300 and status_code < 400:
            print(f"{URL} has {status_code} response code")
        elif status_code >= 400 and status_code < 500:
            print(f"{URL} doesn't exist. {status_code} code")
        else:
            print(f"{status_code} code")

#You can add your own technologies to this list
technologies = [Technology("Wordpress", "/wp-admin"), Technology("Joomla", "/administrator"), Technology("Django", "/admin"), Technology("PHPmyadmin", "/phpmyadmin")]

print("Hello to Admin Panel Searcher")
print("This tool may be quite slow")
print("Type website address: ", end='')
website = input()

for tech in technologies:
    tech.checkPath(website)
print("Thanks for using Admin Panel Searcher")