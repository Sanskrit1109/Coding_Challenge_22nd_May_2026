 #Create a program to check whether a given username and password match predefined credentials.
predefined_username = "admin"
predefined_password = "password123"
username = input("Enter username: ")
password = input("Enter password:")
if username == predefined_username and password == predefined_password:
    print("Login successfully")
else:
    print("Invalid username or password")
    
#Output 1
#Enter username: Sanskriti
#Enter password:sanskriti123
#Invalid username or password

#Output 2
#Enter username: admin
#Enter password:password123
#Login successfully