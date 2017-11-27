PASSWORD = '123'
LOGIN = 'admin'
entered_username = input("enter your username: ")
entered_password = input("enter your password: ")
if entered_password == PASSWORD and entered_username == LOGIN:
    print("Access Granted")
else:
    print("Forbidden")
