"""
43. Write a Python program to get OS name, platform and release information.
"""

import os
import platform

if __name__ == '__main__':
    print(f'OS Name: {os.name}')
    print(f'Platform: {platform.system()}')
    print(f'Release: {platform.release()}')