#! python3

"""
 Have the user enter a username 
 If the username is not "admin" then tell them it is an "invalid user", 
 but if it is, then ask them for a password 
 If they get the password correct (password is 12345password) 
 then display the message "Access granted"
 remember to use .strip() when retrieving strings or you will
 include hidden characters (the carriage return) that will
 not match
 1 marks

 Example:
 Enter username: admin
 Enter password: 12345password
 Access granted

 Enter username: notadmin
 invalid user

 Enter username: admin
 Enter password: password
 Access denied
"""
u = input("enter a username")
p = input("enter a password")
if u == "admin" and p == "12345password":
    print("access granted")

elif u != "admin" and p != "12345password":
    print("access denied")

elif u != "admin":
    print("invaid user")
    
