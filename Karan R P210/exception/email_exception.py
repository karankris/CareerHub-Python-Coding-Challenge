# exception/email_exception.py

# email_exception.py

class EmailFormatException(Exception):
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        self.message = message
        super().__init__(self.message)
