# exception/salary_exception.py

class InvalidSalaryException(Exception):
    def __init__(self, message="Invalid salary value. Salary cannot be negative or zero."):
        self.message = message
        super().__init__(self.message)
