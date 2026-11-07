# INHERITANCE
# Employee -- name, id, department, gender
# Salaried Employee -- salary, tenure
# Casual Workers -- rates


# PARENT CLASS
class Employee:
    def __init__(self, name: str, id_no: str, department: str, gender: str):
        self.fullnames = name
        self.identity = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(f"Full Names : {self.fullnames}")
        print(f"ID Number  : {self.identity}")
        print(f"Department : {self.department}")
        print(f"Gender     : {self.gender}")
        print("------------------------")


# CHILD CLASS 1
class salariedemployee(Employee):
    def __init__(self, name: str, id_no: str, department: str,
                 gender: str, salary: int, tenure: int):

        super().__init__(name, id_no, department, gender)

        self.tenure = tenure
        self.salary = salary

    def print_salary_details(self):
        self.print_details()
        print(f"Monthly Salary : Ksh {self.salary}")
        print(f"Tenure         : {self.tenure} years")
        print("------------------------")


# CHILD CLASS 2
class casualworkers(Employee):
    def __init__(self, name: str, id_no: str, department: str,
                 gender: str, rate: float | int):

        super().__init__(name, id_no, department, gender)

        self.rate = rate

    def calculate_payment(self, hours_worked: int):
        payment = self.rate * hours_worked
        print(f"Hourly Rate    : Ksh {self.rate}")
        print(f"Hours Worked   : {hours_worked}")
        print(f"Total Payment  : Ksh {payment}")

    def print_casual_details(self):
        self.print_details()
        print(f"Hourly Rate : Ksh {self.rate}")
        print("------------------------")


# CREATING OBJECTS

s1 = salariedemployee(
    "Sharon Obiri",
    "12345",
    "HR",
    "Female",
    salary=89000,
    tenure=3
)

c1 = casualworkers(
    "Brian Otieno",
    "67890",
    "IT",
    "Male",
    rate=500
)


# DISPLAY SALARIED EMPLOYEE

print("\n===== SALARIED EMPLOYEE =====")
s1.print_salary_details()


# DISPLAY CASUAL WORKER

print("\n===== CASUAL WORKER =====")
c1.print_casual_details()


# CALCULATE CASUAL WORKER PAYMENT

print("\n===== CASUAL PAYMENT =====")
c1.calculate_payment(8)