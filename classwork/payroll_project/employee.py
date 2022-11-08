from abc import ABC, abstractmethod

class Payroll(ABC):
    @abstractmethod
    def print_payroll(self):
        pass

class Employee():
    id = 0
    first_name = ''
    last_name = ''
    role = ''
    email = ''
    phone_number = ''
    is_active = True
    salary = 0



class FullTimeEmp(Employee, Payroll):
    def print_payroll(self):
       print (f"Employee Name: {self.firstname}, {self.lastname}")
       print (f"Employee Salary: {self.salary}")


class HourlyEmp(Employee, Payroll):
    number_of_hours_worked = 0
    hourly_rate = 0
    def print_payroll(self):
        self.salary = self.number_of_hours_worked * self.hourly_rate
        print (f"Employee Name: {self.firstname}, {self.lastname}")
        print (f"Employee Salary: {self.salary}")


full_time = FullTimeEmp()
full_time.firstname = "John"
full_time.lastname = "Doe"
full_time.salary = 100000
full_time.print_payroll()