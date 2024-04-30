'''Build a Python class to represent a simple banking system. Create a class
for a BankAccount, and another for Customer. The BankAccount class should have
a constructor to initialize the account details (account number, balance,
account type). The Customer class should have a constructor to set the
customer's details (name, age, address) and create a BankAccount object for
each customer. Implement a destructor for both classes to display a message
when objects are destroyed
'''


class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print("Destructor for BankAccount")


class Customer(BankAccount):
    def __init__(self, account_number, balance, account_type, name, age,
                 address):
        super(Customer, self).__init__(account_number, balance, account_type)
        self.name = name
        self.age = age
        self.address = address

    def __del__(self):
        print("Destructor for Customer")
        super().__del__()


def main():
    account_number = 12345
    balance = 50000
    account_type = "saving"
    customer_name = "Rajendra"
    age = 22
    address = "Naya Thimi"

    customer = Customer(account_number, balance, account_type, customer_name,
                        age, address)
    del customer


main()
