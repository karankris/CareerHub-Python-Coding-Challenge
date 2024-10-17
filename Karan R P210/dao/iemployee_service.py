# dao/iemployee_service.py
from abc import ABC, abstractmethod

class IEmployeeService(ABC):
    @abstractmethod
    def add_employee(self, employee):
        """
        Adds a new employee to the database.
        :param employee: Employee object containing employee details.
        """
        pass

    @abstractmethod
    def get_employee(self, employee_id):
        """
        Retrieves an employee's information from the database.
        :param employee_id: Unique ID of the employee.
        :return: Employee object containing employee details.
        """
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        """
        Deletes an employee from the database.
        :param employee_id: Unique ID of the employee.
        """
        pass

    @abstractmethod
    def update_employee(self, employee):
        """
        Updates an existing employee's information in the database.
        :param employee: Employee object containing updated details.
        """
        pass
