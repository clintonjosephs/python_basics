class IBM:
    def get_processor_speed(self):
        print(f"16GHZ")

    def login(self, username, password, otp = None, key_code = None):
        print(f"Logging in with username: {username} and password: {password}")

    def registration(self, email, password, phone = None, year_of_birth = None):
        print(f"Email: {email}")
        print(f"Password: {password}")
        if (phone != None):
            print(f"Phone: {phone}")
        if (year_of_birth != None):
            print(f"Year of birth: {year_of_birth}")

class HP(IBM):
    def get_processor_speed(self):
        print(f"32GHZ")

ibm = IBM()
ibm.get_processor_speed()

ibm.registration("clintonmbonu@meltwater.org", "password", "0700000000", "1990")

hp = HP()
hp.get_processor_speed()