# Ankit BroCheck
# Make list and and print it using while loop

# Rupesh  BroCheck
# create a input for name and email and password and confirm password for terminal login and pre store some data to for conformation of user login

# Manish BroCheck
# i have done some work in python as you asked for

print("Enter your name :")
name = input()

print("Enter you EmailId :")
email = input()

print("Enter a password : ")
password = input()

print("Hello, ", name, " your eamil is ",
      email, " and your password is ", password)

print("enter your password : ")
check_pass = input()

if (check_pass == password):
    print("login successful")
else:
    print("wrong password ")
