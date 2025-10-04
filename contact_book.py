#function made to store contact info
def add_contact(contact_list):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    new_contact = {'name': name,'phone': phone}
    contact_list.append(new_contact)
    
    print(f"Contact for {name} added successfully.")
    
def view_contact(contact_list):
    for contact in contact_list:
        print(f"Name: {contact['name']} | Phone: {contact['phone']}")
    
    

def main():
    contacts = []
    while True:
        choice = input("What would you like to do with your contact book? (add, view, quit): ")
        if choice == "quit":
            break
        elif choice == "view":
            view_contact(contacts)
        elif choice == "add":
            add_contact(contacts)
        else:
            print("Not a valid selection! Try Again")
        
main()
