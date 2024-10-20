from contact import Contact
from contact_book import ContactBook

primary_book = ContactBook()

while True:
    choice = input(f"Add, View or Remove. Please select an option \n").lower()
    if choice == 'add':
        name = input('please choose name').title()
        phone = int(input('please add number'))
        email = input('please add email')
        contact = Contact(name,phone,email)
        primary_book.add_contact(contact)
    elif choice == 'view':
        pass
    else: 
        pass

"""Plan for CLI (main.py):
Main Menu: Display options to the user (e.g., Add, View, Remove contacts).
User Input: The program will capture what the user wants to do.
Call Methods: Based on the input, you’ll call the appropriate methods from ContactBook (like adding a contact or viewing all contacts).
Steps:
Main Menu: Write a function that shows a menu with options (Add, View, Remove, etc.).
User Input Handling: Capture the user’s input (e.g., they select "1" to add a contact).
Method Calls: Call the appropriate method from ContactBook.
Example Breakdown (in main.py):
Display Menu:

Show options like "Add a contact", "Remove a contact", etc.
Handle Input:

Ask the user to choose an option from the menu.
Call Methods:

Based on the user's choice, call methods like add_contact, view_contact from the ContactBook."""