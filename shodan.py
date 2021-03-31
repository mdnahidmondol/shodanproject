import shodan

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