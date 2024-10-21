from contact import Contact
from contact_book import ContactBook

primary_book = ContactBook()

user = Contact('Zain',424242,'zain@email.com')

primary_book.add_contact(user)


while True:
    choice = input(f"\nAdd, View, Update, Remove or Quit. Please select an option \n").lower()
    if choice == 'add':
        name = input('please choose name').title()
        phone = input('please add number')
        email = input('please add email')
        contact = Contact(name, phone, email)
        primary_book.add_contact(contact)
    elif choice == 'view':
        primary_book.view_contact()
    elif choice == 'remove':
        primary_book.remove_contact()
    elif choice == 'update':
        primary_book.update_contact()
        print("Record updated")
    elif choice == "quit":
        break 
    else: print("Sorry input not recognized")

