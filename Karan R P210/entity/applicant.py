# entity/applicant.py
class Applicant:
    def __init__(self, applicant_id, first_name, last_name, email, phone, resume):
        """
        Constructor to initialize the Applicant object with necessary details.
        :param applicant_id: Unique ID of the applicant.
        :param first_name: First name of the applicant.
        :param last_name: Last name of the applicant.
        :param email: Email address of the applicant.
        :param phone: Phone number of the applicant.
        :param resume: Path or reference to the resume file.
        """
        self.applicant_id = applicant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume

    def create_profile(self):
        """
        Simulates the creation of an applicant profile with their contact information.
        Prints a summary of the applicant's profile.
        """
        profile_summary = (
            f"Profile created for {self.first_name} {self.last_name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Resume Path: {self.resume}\n"
        )
        print(profile_summary)

    def update_resume(self, new_resume):
        """
        Updates the resume for the applicant.
        :param new_resume: New path or reference to the updated resume file.
        """
        self.resume = new_resume
        print(f"Resume updated to: {self.resume}")

    def __str__(self):
        """
        Returns a string representation of the applicant's profile.
        """
        return f"{self.first_name} {self.last_name} (ID: {self.applicant_id})"
