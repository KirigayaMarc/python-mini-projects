#Simple Age Verification gatekeeper mini project

age = int(input("Please enter your age: "))

if age >= 18:
    print("Access Granted.")
else:
    print("Access Denied.")