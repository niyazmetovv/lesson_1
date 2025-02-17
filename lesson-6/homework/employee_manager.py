def add_employee():
    with open("employees.txt", "a") as file:
        id = input("EnterID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        all_info = id + ", " + name + ", " + position + ", " + salary + '\n'
        file.write(all_info)

def view_employees():
    with open("employees.txt", "r") as file:
        print(file.read())

def search_employees(id):
        with open("employees.txt", "r") as file:
            all_lines = file.readlines()
            for line in all_lines:
                list = line.strip().split(", ")
                if list[0] == str(id):
                    return line.strip()
            return False

def update_employees(id):
    employee = search_employees(id)
    if not employee:
        print("ID not found")
        return 0
    else:
        with open("employees.txt", "r") as file:
            all_lines = file.readlines()
        with open("employees.txt", 'w') as file:
            for line in all_lines:
                list = line.strip().split(", ")
                if list[0] == str(id):
                    list[1] = input("Enter new name: ")
                    list[2] = input("Enter new position: ")
                    list[3] = input("Enter new salary: ")
                    updated_line = ", ".join(list) + '\n'
                    file.write(updated_line)
                else:
                    file.write(line)

def delete_employees(id):
    employee = search_employees(id)
    if not employee:
        print("ID not found")
        return 0
    else:
        with open("employees.txt", "r") as file:
            all_lines = file.readlines()
        with open("employees.txt", 'w') as file:
            for line in all_lines:
                list = line.strip().split(", ")
                if list[0] == str(id):
                    continue
                else:
                    file.write(line)





print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")

while True:
    decision = input("Enter number: ")
    if decision == "1":
        add_employee()
    elif decision == "2":
        view_employees()
    elif decision == "3":
        id = int(input("Enter ID: "))
        search_employees(id)
    elif decision == "4":
        id = int(input("Enter ID: "))
        update_employees(id)
    elif decision == "5":
        id = int(input("Enter ID: "))
        delete_employees(id)
    elif decision == "6":
        break
    else:
        print("Invalid input")
