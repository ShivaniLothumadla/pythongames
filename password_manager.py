"""
one master password
one file to read/write/append the passwords
add method for write/append to the file
view method for view the passwords from the file
"""
from cryptography.fernet import Fernet
def add():
    site_name = input("enter the site name: ")
    name = input("enter the user name: ")
    pwd = input("enter the password: ")
    with open('creds.txt', 'a') as f:
        f.write(site_name + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('creds.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            sitename, username, pswd = data.split('|')
            print("sitename:", sitename + " | " + "user:", username + " | " + "password:", fer.decrypt(pswd.encode()).decode())

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
        return key
# write_key()
mastser_pwd = input("enter the master password: ")
key = load_key() + mastser_pwd.encode()
fer = Fernet(key)
while True:
    mode = input("Would you like to add/view or quit [add/view/q]? ")
    if mode == 'q':
        break
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Invalid mode!!")
        continue
