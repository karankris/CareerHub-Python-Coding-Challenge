from dao.database_manager import DatabaseManager
from entity.applicant import Applicant
from entity.company import Company
from entity.job_listing import JobListing
from entity.job_application import JobApplication

def main():
    db_manager = DatabaseManager()

    while True:
        print("Job Board Application")
        print("1. Insert Applicant")
        print("2. Insert Company")
        print("3. Insert Job Listing")
        print("4. Insert Job Application")
        print("5. View All Applicants")
        print("6. View All Job Listings")
        print("7. View All Job Applications")
        print("8. View All Companies")
        print("9. Exit")

        choice = input("Enter your choice: ")

        
        if choice == '1':
            # Insert Applicant
            applicant_id = int(input("Enter Applicant ID: "))  # Get Applicant ID from the user
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            resume = input("Enter Resume file path: ")

            # Create Applicant object
            applicant = Applicant(applicant_id, first_name, last_name, email, phone, resume)  # Include applicant_id
            
            # Insert into the database
            db_manager.insert_applicant(applicant)

        elif choice == '2':
            # Insert Company
            company_id = int(input("Enter Company ID: "))
            company_name = input("Enter Company Name: ")
            location = input("Enter Location: ")

            # Create Company object
            company = Company(company_id, company_name, location)
            
            # Insert into the database
            db_manager.insert_company(company)

        elif choice == '3':
            # Insert Job Listing
            job_id = int(input("Enter Job ID: "))
            company_id = int(input("Enter Company ID: "))
            job_title = input("Enter Job Title: ")
            job_description = input("Enter Job Description: ")
            job_location = input("Enter Job Location: ")
            salary = float(input("Enter Salary: "))
            job_type = input("Enter Job Type: ")
            posted_date = input("Enter Posted Date (YYYY-MM-DD): ")

            # Create JobListing object
            job_listing = JobListing(job_id, company_id, job_title, job_description, job_location, salary, job_type, posted_date)
            
            # Insert into the database
            db_manager.insert_job_listing(job_listing)

        elif choice == '4':
            # Insert Job Application
            application_id = int(input("Enter Application ID: "))
            job_id = int(input("Enter Job ID: "))
            applicant_id = int(input("Enter Applicant ID: "))
            application_date = input("Enter Application Date (YYYY-MM-DD): ")
            cover_letter = input("Enter Cover Letter: ")

            # Create JobApplication object
            job_application = JobApplication(application_id, job_id, applicant_id, application_date, cover_letter)
            
            # Insert into the database
            db_manager.insert_job_application(job_application)

        elif choice == '5':
            # View All Applicants
            applicants = db_manager.get_all_applicants()
            for applicant in applicants:
                print(f"ID: {applicant.ApplicantID}, Name: {applicant.FirstName} {applicant.LastName}, Email: {applicant.Email}")

        elif choice == '6':
            # View All Job Listings
            job_listings = db_manager.get_all_job_listings()
            for job in job_listings:
                print(f"Job ID: {job.JobID}, Title: {job.JobTitle}, Location: {job.JobLocation}, Salary: {job.Salary}")

        elif choice == '7':
            # View All Job Applications
            job_applications = db_manager.get_all_job_applications()
            for app in job_applications:
                print(f"Application ID: {app.ApplicationID}, Job ID: {app.JobID}, Applicant ID: {app.ApplicantID}, Date: {app.ApplicationDate}")
        elif choice == '8':
            companies = db_manager.get_all_companies()
            for app in companies:
                print(f"Company ID: {app.CompanyID} ,CompanyName: {app.CompanyName}, Location: {app.Location}")
        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
