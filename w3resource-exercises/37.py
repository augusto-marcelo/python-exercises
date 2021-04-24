"""
37. Write a Python program to display your details like name, age, address in three different lines.
"""


def get_user_data():

    name = input("Your name: ")
    age = input("Your age: ")
    address = input("Your address: ")

    user_dict = dict()

    user_dict['name'] = name
    user_dict['age'] = age
    user_dict['address'] = address

    for key in user_dict.keys():
        print(f"{key} : {user_dict.get(key)}")



if __name__ == '__main__':
    get_user_data()