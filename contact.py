class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def update(self, element, change):
        if element == 'name':
            self.name = change
        elif element == 'phone':
            self.phone = change
        elif element == 'email':
            self.email = change
        else: print ("Sorry that field doesn't exist")
        

    def get_details(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
