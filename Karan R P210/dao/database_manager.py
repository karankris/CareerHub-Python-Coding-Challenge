import pyodbc
from util.db_conn_util import DBConnUtil
from entity.applicant import Applicant
from entity.company import Company
from entity.job_listing import JobListing
from entity.job_application import JobApplication

class DatabaseManager:
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    # Insert applicant into Applicants table
    def insert_applicant(self, applicant: Applicant):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            # Pass applicant_id first
            cursor.execute(query, (
                applicant.applicant_id, 
                applicant.first_name, 
                applicant.last_name, 
                applicant.email, 
                applicant.phone, 
                applicant.resume
            ))
            self.connection.commit()
            print("Applicant inserted successfully.")
        except pyodbc.Error as e:
            print(f"Failed to insert applicant: {e.args}")
            raise
        finally:
            cursor.close()

    # Insert company into Companies table
    def insert_company(self, company: Company):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Companies (CompanyID, CompanyName, Location)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (company.company_id, company.company_name, company.location))
            self.connection.commit()
            print("Company inserted successfully.")
        except pyodbc.Error as e:
            print(f"Failed to insert company: {e.args}")
            raise
        finally:
            cursor.close()

    # Insert job listing into Jobs table
    def insert_job_listing(self, job_listing: JobListing):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Jobs (JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                job_listing.job_id, 
                job_listing.company_id, 
                job_listing.job_title,
                job_listing.job_description, 
                job_listing.job_location, 
                job_listing.salary,
                job_listing.job_type, 
                job_listing.posted_date
            ))
            self.connection.commit()
            print("Job listing inserted successfully.")
        except pyodbc.Error as e:
            print(f"Failed to insert job listing: {e.args}")
            raise
        finally:
            cursor.close()

    # Insert job application into Applications table
    def insert_job_application(self, job_application: JobApplication):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Applications (ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                job_application.application_id, 
                job_application.job_id,
                job_application.applicant_id, 
                job_application.application_date,
                job_application.cover_letter
            ))
            self.connection.commit()
            print("Job application inserted successfully.")
        except pyodbc.Error as e:
            print(f"Failed to insert job application: {e.args}")
            raise
        finally:
            cursor.close()

    # Retrieve all applicants
    def get_all_applicants(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Applicants"
            cursor.execute(query)
            applicants = cursor.fetchall()
            return applicants
        except pyodbc.Error as e:
            print(f"Failed to retrieve applicants: {e.args}")
            raise
        finally:
            cursor.close()

    # Retrieve all job listings
    def get_all_job_listings(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Jobs"
            cursor.execute(query)
            job_listings = cursor.fetchall()
            return job_listings
        except pyodbc.Error as e:
            print(f"Failed to retrieve job listings: {e.args}")
            raise
        finally:
            cursor.close()

    # Retrieve all job applications
    def get_all_job_applications(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Applications"
            cursor.execute(query)
            job_applications = cursor.fetchall()
            return job_applications
        except pyodbc.Error as e:
            print(f"Failed to retrieve job applications: {e.args}")
            raise
        finally:
            cursor.close()
            
               # Retrieve all company
    def get_all_companies(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Companies"
            cursor.execute(query)
            applicants = cursor.fetchall()
            return applicants
        except pyodbc.Error as e:
            print(f"Failed to retrieve Companies: {e.args}")
            raise
        finally:
            cursor.close()
