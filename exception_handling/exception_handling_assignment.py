import logging

logger_warning = logging.getLogger(__name__)
logger_warning.setLevel(logging.WARNING)

logger_info = logging.getLogger(__name__)
logger_info.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('exception-handling.log')
file_handler.setFormatter(formatter)
logger_warning.addHandler(file_handler)
logger_info.addHandler(file_handler)

'''Write a Python program that takes two integers as input and performs
division (num1 / num2). Handle the ZeroDivisionError and display a custom
error message when the second number is zero
'''


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        logger_info.info(f"Result of division: {result}")
    except ZeroDivisionError:
        logger_warning.warning("Error!! Division by zero is not allowed!")


divide_numbers(50, 5)


'''Implement a program that takes user input for a filename, opens the file
in read mode, and displays its contents. Handle the FileNotFoundError and
display an error message if the file is not found
'''


def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                logger_info.info(line)
    except FileNotFoundError:
        logger_warning.warning("File not found.")


# def main():
#     filename = input("Enter the filename: ")
#     display_file_contents(filename)


'''Write a Python program that takes a user input and converts it to an
integer. Handle the ValueError and display a custom error message when the
input cannot be converted to an integer
'''


def convert_to_integer(user_input):
    try:
        num = float(user_input)
        num = int(num)
        logger_info.info("Converted integer:", num)
    except ValueError:
        logger_warning.warning("cannot convert to an integer.")


# def main():
#     user_input = input("Enter a number: ")
#     convert_to_integer(user_input)


'''Write a Python program that takes two integers as input and performs
division (num1 / num2). Handle both ValueError (if non-integer input) and
ZeroDivisionError and display appropriate error messages.
'''


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        logger_info.info(f"Result of division: {result}")
    except ZeroDivisionError:
        logger_warning.warning("Division by zero is not allowed!")


# def main():
#     try:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         divide_numbers(num1, num2)
#     except ValueError:
#         logger_warning.warning("Please enter valid integers.")


'''Write a Python program that takes user input for age. Create a custom
exception InvalidAgeError to handle cases where the age is below 0 or above
120
'''


class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0 or age > 120:
        message = "Age must be between 0 and 120."
        logger_warning.warning(message)
        raise InvalidAgeError(message)


# def main():
#     age = int(input("Enter your age: "))
#     check_age(age)
#     logger_info.info(f"Your age is: {age}")


'''Implement a program that reads user input for a password. Create a custom
exception WeakPasswordError to handle cases where the password is shorter than
8 characters
'''


class WeakPasswordError(Exception):
    pass


def check_password(password):
    if len(password) < 8:
        message = "Password is shorter than 8 characters."
        logger_warning.warning(message)
        raise WeakPasswordError(message)
    else:
        logger_info.info(f"password: {password}")


def main():
    password = input("Enter your password: ")
    check_password(password)
