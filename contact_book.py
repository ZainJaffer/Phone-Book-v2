class ContactBook:

    def __init__(self):
        self.book = {}

    def add_contact(self,contact):
        self.book[contact.name] = contact

    def remove_contact(self):
        self.view_contact()
        name = input('\nPlease type name of user you want to remove \n').title() 
        if name in self.book:
            print("contact found")
            del self.book[name]
            print("contact removed")

    def update_contact(self):
        pass

    def view_contact(self):
        if self.book:
            print(f"Here is the full list of contacts in the book:\n")
            for key, contacts in self.book.items():
                print(contacts.get_details())
        else: print("There are currently no contacts to view")