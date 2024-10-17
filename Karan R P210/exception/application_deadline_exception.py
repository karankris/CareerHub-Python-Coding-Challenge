# exception/application_deadline_exception.py

class ApplicationDeadlineException(Exception):
    def __init__(self, message="The job application deadline has passed. No further applications are accepted."):
        self.message = message
        super().__init__(self.message)
