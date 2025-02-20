import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.name = name
        self.salary = salary
        self.employee_id =employee_id
        self.position = position

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager():
    file = "employee.txt"
    def __init__(self):
        if not os.path.exists(self.file):
            open(self.file, "w").close()

    def search_employee(self, employee_id):
        with open(self.file, "r") as f:
            for line in f:
                separated = line.strip().split(", ")
                if separated[0] == str(employee_id):
                    print("Employee Found:")
                    print(line.strip())
                    return True
            print("Employee not found.")
            return False

    def unique_id_checker(self, employee_id):
        with open(self.file, "r") as f:
            lines = f.readlines()
            for line in lines:
                separated = line.strip().split(", ")
                if separated[0] == str(employee_id):
                    return False
            else:
                return True

    def add_employee(self, employee):
      if self.unique_id_checker(employee.employee_id):
          with open(self.file, "a") as f:
            f.write(str(employee) + '\n')
          print("Employee added successfully!")
      else:
          print("Employee already added!")
    def view_all_employees(self):
        try:
         with open(self.file, "r") as f:
            print("Employee Records: ")
            print(f.read().strip())
        except FileNotFoundError:
            print("Employee Records file not found.")


    def update_employee(self, employee_id):
        if self.search(employee_id):
            new_id = int(input("Enter new employee ID: "))
            new_name = input("New name : ")
            new_position = input("New position : ")
            new_salary = float(input("New salary : "))
            with open(self.file, 'r') as f:
                all_info = f.readlines()
            with open(self.file, "w") as file:
                for line in all_info:
                    separated = line.strip().split(", ")
                    if separated[0] == employee_id:
                            file.write(f"{str(new_id)}, {new_name}, {new_position}, {new_salary}\n")
                    else:
                            file.write(line)
            print("Employee updated successfully!")
        else:
            return
    def delete_employee(self, employee_id):
        with open(self.file, "r") as f:
            all_info = f.readlines()
            with open(self.file, "w") as file:
                for line in all_info:
                    separated = line.strip().split(", ")
                    if separated[0] == employee_id:
                        continue
                    else:
                        file.write(line)
        print("Employee deleted successfully!")



print("""
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
handler = EmployeeManager()
while True:

    n = int(input())
    if n == 1:
        id = int(input("Enter employee ID : "))
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = int(input("Enter employee salary: "))
        employee = Employee(id, name, position, salary)
        if isinstance(id, int) or isinstance(name, str) or isinstance(position, str) or isinstance(salary, int):
         handler.add_employee(employee)
        else:
            print("Invalid input.")
    elif n == 2:
        handler.view_all_employees()
    elif n == 3:
        id = input("Enter employee ID : ")
        handler.search_employee(id)
    elif n == 4:
        id = input("Enter employee ID : ")
        handler.update_employee(id)
    elif n == 5:
        id = input("Enter employee ID : ")
        handler.delete_employee(id)
    elif n == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid input")
