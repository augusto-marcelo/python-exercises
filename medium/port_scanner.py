"""
Custom Python Port Scanncer (exercise)

Based on Medium article: 
    Title: Port Scanner With Python
        Sub-title: A Simple Port Scanner Using Python.
    https://imrajeshberwal.medium.com/port-scanner-with-python-edd53788c5bb
"""

import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#Defining a target
if len(sys.argv) == 2:
    
    #translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    target = socket.gethostbyname('localhost')
    print("Invalid ammount of Argument")


# Add banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try: 
    # will scan ports between 1 to 65.535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #return an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !!!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could not be resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!")
    sys.exit()