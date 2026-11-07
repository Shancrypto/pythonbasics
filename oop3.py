# CLASSES

# CUSTOMER CLASS
class Customer:
    def __init__(self, names: str, age: int, city: str,
                 email: str, dob: str, gender: str, kra: str):

        self.name = names
        self.age = age
        self.city = city
        self.email = email
        self.dob = dob
        self.gender = gender
        self.kra = kra

    def show_details(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"City       : {self.city}")
        print(f"Email      : {self.email}")
        print(f"DOB        : {self.dob}")
        print(f"Gender     : {self.gender}")
        print(f"KRA PIN    : {self.kra}")


# BANK ACCOUNT CLASS
class Account:
    def __init__(self, owner: Customer, acc_no: str,
                 balance: float | int, acc_type: str):

        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance
        self.acc_type = acc_type

    def print_details(self):
        print(f"Owner        : {self.owner.name}")
        print(f"Balance      : Ksh {self.balance}")
        print(f"Account Type : {self.acc_type}")
        print(f"Account No.  : {self.acc_no}")
        print("************************")

    def deposit(self, amount: float | int):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print(f"Successfully deposited Ksh {amount}")
            print(f"New Balance: Ksh {self.balance}")

    def withdraw(self, amount: float | int):
        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            print(f"Successfully withdrawn Ksh {amount}")
            print(f"Remaining Balance: Ksh {self.balance}")


# CREATING CUSTOMER OBJECTS

customer1 = Customer(
    "Sharon Obiri",
    21,
    "Kisii",
    "sharon@gmail.com",
    "2005-04-12",
    "Female",
    "A001234567B"
)

customer2 = Customer(
    "Brian Otieno",
    23,
    "Nairobi",
    "brian@gmail.com",
    "2003-06-15",
    "Male",
    "A009876543C"
)


# CREATING BANK ACCOUNT OBJECTS

account1 = Account(customer1, "ACC001", 15000, "Savings")

account2 = Account(customer2, "ACC002", 25000, "Current")


# DISPLAY CUSTOMER DETAILS

print("\n===== CUSTOMER DETAILS =====")

customer1.show_details()

print("\n===== BANK ACCOUNT DETAILS =====")

account1.print_details()


# DEPOSIT MONEY

print("\n===== DEPOSIT TRANSACTION =====")

account1.deposit(5000)


# WITHDRAW MONEY

print("\n===== WITHDRAWAL TRANSACTION =====")

account1.withdraw(2000)


# DISPLAY UPDATED ACCOUNT DETAILS

print("\n===== UPDATED ACCOUNT DETAILS =====")

account1.print_details()


# DISPLAY SECOND CUSTOMER ACCOUNT

print("\n===== SECOND CUSTOMER ACCOUNT =====")

account2.print_details()