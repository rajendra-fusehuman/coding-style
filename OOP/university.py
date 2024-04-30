'''Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement
encapsulation to protect the internal data of the University class. Create a
Department class that inherits from the University class. The Department class
should have attributes like department name, head of the department, and a
list of courses offered. Implement polymorphism by defining a common method
for both the University and Department classes to display their details.
'''


class University:
    def __init__(self, name, location, departments):
        self.name = name
        self.location = location
        self.departments = departments

    def view_details(self):
        print("University Details:")
        print(f"Name of the university: {self.name}")
        print(f"Location: {self.location}")
        print(f"Departments: {self.departments}")


class Department(University):
    def __init__(self, university_name, location, departments, department_name,
                 HOD, courses_offered):
        super(Department, self).__init__(university_name, location,
                                         departments)
        self.department_name = department_name
        self.HOD = HOD
        self.courses_offered = courses_offered

    def view_details(self):
        University.view_details(self)
        print("\nDeparment Details:")
        print(f"Name of the department: {self.department_name}")
        print(f"HOD: {self.HOD}")
        print(f"Courses Offered: {self.courses_offered}")


def main():
    departments = ["applied science", "mathematics", "literature"]
    courses_offered = ["BCT", "BEI", "BCE", "BME"]

    # university = University("TU", "kirtipur", departments)
    department = Department("TU", "kirtipur", departments, "applied science",
                            "Kiran Dahal", courses_offered)
    department.view_details()


if __name__ == "__main__":
    main()
