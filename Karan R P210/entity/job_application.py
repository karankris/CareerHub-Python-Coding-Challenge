# entity/job_application.py
from datetime import datetime

class JobApplication:
    def __init__(self, application_id, job_id, applicant_id, application_date, cover_letter):
        """
        Constructor to initialize the JobApplication object with necessary details.
        :param application_id: Unique ID of the job application.
        :param job_id: Reference to the JobListing (JobID).
        :param applicant_id: Reference to the Applicant (ApplicantID).
        :param application_date: Date when the application was submitted.
        :param cover_letter: Cover letter submitted with the job application.
        """
        self.application_id = application_id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.application_date = application_date
        self.cover_letter = cover_letter

    def apply_for_job(self):
        """
        Simulates applying for a job by submitting an application with a cover letter.
        """
        print(f"Application {self.application_id} submitted by applicant {self.applicant_id} for job {self.job_id}.")
