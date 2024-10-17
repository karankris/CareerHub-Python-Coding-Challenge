# dao/employee_service.py

from dao.database_manager import DatabaseManager
from dao.iemployee_service import IEmployeeService
import pyodbc

class EmployeeServiceImpl(IEmployeeService):
    def add_employee(self, employee):
        """
        Adds a new employee to the database.
        :param employee: Employee object containing employee details.
        """
        conn = DatabaseManager.get_connection()
        if conn is None:
            return

        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Employees (employee_id, first_name, last_name, email, phone, department, salary)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (employee.employee_id, employee.first_name, employee.last_name, employee.email, employee.phone, employee.department, employee.salary))
            conn.commit()
            print(f"Employee {employee.first_name} {employee.last_name} added successfully.")
        except pyodbc.Error as e:
            print(f"Error adding employee: {e}")
        finally:
            cursor.close()
            conn.close()

    def get_employee(self, employee_id):
        """
        Retrieves an employee's information from the database.
        :param employee_id: Unique ID of the employee.
        :return: Employee object containing employee details.
        """
        conn = DatabaseManager.get_connection()
        if conn is None:
            return None

        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT * FROM Employees WHERE employee_id = ?
            ''', employee_id)
            row = cursor.fetchone()
            if row:
                employee = {
                    "employee_id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "department": row[5],
                    "salary": row[6]
                }
                return employee
            else:
                print(f"Employee with ID {employee_id} not found.")
                return None
        except pyodbc.Error as e:
            print(f"Error fetching employee: {e}")
        finally:
            cursor.close()
            conn.close()

    def delete_employee(self, employee_id):
        """
        Deletes an employee from the database.
        :param employee_id: Unique ID of the employee.
        """
        conn = DatabaseManager.get_connection()
        if conn is None:
            return

        cursor = conn.cursor()
        try:
            cursor.execute('''
                DELETE FROM Employees WHERE employee_id = ?
            ''', employee_id)
            conn.commit()
            print(f"Employee with ID {employee_id} deleted successfully.")
        except pyodbc.Error as e:
            print(f"Error deleting employee: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_employee(self, employee):
        """
        Updates an existing employee's information in the database.
        :param employee: Employee object containing updated details.
        """
        conn = DatabaseManager.get_connection()
        if conn is None:
            return

        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE Employees SET first_name = ?, last_name = ?, email = ?, phone = ?, department = ?, salary = ?
                WHERE employee_id = ?
            ''', (employee.first_name, employee.last_name, employee.email, employee.phone, employee.department, employee.salary, employee.employee_id))
            conn.commit()
            print(f"Employee {employee.first_name} {employee.last_name} updated successfully.")
        except pyodbc.Error as e:
            print(f"Error updating employee: {e}")
        finally:
            cursor.close()
            conn.close()
