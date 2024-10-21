class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.book = {}

    def update(self):
        pass

    def get_details(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
