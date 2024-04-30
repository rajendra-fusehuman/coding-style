import pandas as pd
import json

'''Implement a program that reads a CSV file named "data.csv," containing
columns "Name" and "Age." Create a new CSV file called "adults.csv" with only
the rows of individuals who are 18 years or older
'''


def modify_csv():
    df = pd.read_csv(FILE_NAME)
    new_df = df[df['Age'] >= 18]
    new_df.to_csv(NEW_FILE_NAME, index=False)


FILE_NAME = "data.csv"
NEW_FILE_NAME = "adults.csv"


'''Create a function add_to_json that takes a filename and a dictionary as
input. The function should read the JSON data from the file, add the new
dictionary to it, and write the updated data back to the same file
'''


def add_to_json(filename, dictionary):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(dictionary)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


'''Create a function search_log that takes a log file and a search keyword as
input. The function should find and display all lines containing the search
keyword
'''


def search_log(log_file, search_keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if search_keyword in line:
                    print(line)
    except FileNotFoundError:
        print("Error!! file not found.")
