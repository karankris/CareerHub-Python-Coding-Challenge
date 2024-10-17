# entity/job_listing.py
from datetime import datetime

class JobListing:
    def __init__(self, job_id, company_id, job_title, job_description, job_location, salary, job_type, posted_date):
        """
        Constructor to initialize the JobListing object with necessary details.
        :param job_id: Unique ID of the job listing.
        :param company_id: Reference to the Company (CompanyID) that posted the job.
        :param job_title: Title of the job.
        :param job_description: Detailed description of the job.
        :param job_location: Location where the job is based.
        :param salary: Salary offered for the job.
        :param job_type: Type of job (e.g., Full-time, Part-time, Contract).
        :param posted_date: Date when the job was posted.
        """
        self.job_id = job_id
        self.company_id = company_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.posted_date = posted_date

    def apply(self, applicant_id, cover_letter):
        """
        Simulates applying for this job by an applicant.
        :param applicant_id: ID of the applicant applying for the job.
        :param cover_letter: The cover letter submitted by the applicant.
        """
        print(f"Applicant {applicant_id} applied for job {self.job_id} with cover letter: {cover_letter}")

    def get_applicants(self):
        """
        Simulates retrieving a list of applicants who applied for this job.
        """
        print(f"Fetching applicants for job {self.job_id}.")
