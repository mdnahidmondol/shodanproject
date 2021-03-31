import  shodan
import pyfiglet
from pyfiglet import Figlet

custom_fig = Figlet(font='block')
print(custom_fig.renderText('DevSkill'))

ascii_banner = pyfiglet.figlet_format("          Dev Skill ")
print(ascii_banner)



apikey= "cfi2YdrRLewqAeghYWD46XeXTzWHGUeW"

import sys 
ip = "165.22.99.37"
try:
    api = shodan.Shodan(apikey)
    result = api.host(ip)
    print(ip, result['org'])
except Exception as e:
    print('Error: %s %e')
    sys.exit(1)