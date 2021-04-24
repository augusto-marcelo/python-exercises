"""
54. Write a Python program to get the current username
"""

import os
import getpass #answer from the site

username = os.environ.get('USERNAME')
user = getpass.getuser()

print(f'Username = {username}')
print(f'User={user}')

passwd = getpass.getpass()
print(passwd)