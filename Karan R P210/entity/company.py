# entity/company.py
class Company:
    def __init__(self, company_id, company_name, location):
        """
        Constructor to initialize the Company object with necessary details.
        :param company_id: Unique ID of the company.
        :param company_name: Name of the company.
        :param location: Location of the company.
        """
        self.company_id = company_id
        self.company_name = company_name
        self.location = location

    def post_job(self, job_title, job_description, job_location, salary, job_type):
        """
        Simulates the process of posting a new job by a company.
        :param job_title: Title of the job being posted.
        :param job_description: Description of the job.
        :param job_location: Location where the job is based.
        :param salary: Salary offered for the job.
        :param job_type: Type of job (e.g., Full-time, Part-time, Contract).
        """
        print(f"Job '{job_title}' posted by {self.company_name} in {self.job_location}.")
