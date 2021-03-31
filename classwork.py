

import shodan
import pyfiglet
from pyfiglet import Figlet

custom_fig = Figlet(font='block')
print(custom_fig.renderText('DevSkill'))

ascii_banner = pyfiglet.figlet_format("          Dev Skill ")
print(ascii_banner)





print ("Author: Md Nahid Mondol")
print ("Members Devskil")
print ("fb.com/nahidmondol444")
print ("github.com/")
print ("[!] Legal Disclaimer: We aren't responsible for bad use of this tool!")
print ("")


SHODAN_API_KEY = "cfi2YdrRLewqAeghYWD46XeXTzWHGUeW"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('nginx')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError as e:
        print('Error:')

