"""
53. Write a python program to access environment variables.
"""
import os

# My solution
#for env_var_name in os.environ.items():
    #print(f'{env_var_name[0]}={env_var_name[1]}')

# solution proposed in the comments sections
for ev in os.environ:
    print(f'{ev}={os.environ[ev]}')