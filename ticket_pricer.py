#Simple movie ticket pricer based on age using simple if/else/elif conditions

age = int(input("What is your age? "))

child = age < 13
senior = age >= 65

if child:
    print("Your ticket is $7")
elif senior:
    print("Your ticket is $9")
else:
    print("Your ticket is $12")