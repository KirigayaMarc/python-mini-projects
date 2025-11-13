# creates a grocery list item by item

#create a empty list.
grocery_list = []

while True:
    item = input("Enter a grocery item(or type 'done' to finish):")
    if item == "done":
        break  #ends program
    else:
        grocery_list.append(item) #adds the input from item to the empty list.

if len(grocery_list) > 0:
    print("Here is your grocery list:")  #prints out the grocery list if the number of elements inside the list is greater than 0. 
    for item in grocery_list:
        print(f"* {item}") #prints out the items inputted. 