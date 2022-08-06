original_username, original_password = 'shivani', 12345
username = input("please enter the username: ")
password = int(input("please enter the password: "))
if username == '' and password is None:
    print("username and password is required.")
elif username == '' and password is not None:
    print("username is required.")
elif username != '' and password is None:
    print("password is required.")
elif username == original_username and password == original_password:
    print("Login successful.")
elif username != original_username or password != original_password:
    print("Login unsuccessful.")
