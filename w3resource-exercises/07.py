"""
7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""

file_name = input("Type the filename with the extension: ")

ext = file_name[file_name.find(".") + 1:]

print(ext)