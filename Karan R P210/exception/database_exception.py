# exception/database_exception.py

class DatabaseException(Exception):
    def __init__(self, message="An error occurred with the database operation."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(DatabaseException):
    def __init__(self, message="Failed to connect to the database. Please check your connection settings."):
        super().__init__(message)

class DatabaseQueryException(DatabaseException):
    def __init__(self, message="An error occurred while executing the database query."):
        super().__init__(message)
