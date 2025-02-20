import os
import json

class Tasks():
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class Tasks_management:
    def __init__(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write("")
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task.to_dict())
        print("Successfully added task")

    def view_tasks(self):
        print("View tasks")
        for task in self.tasks:
            print(f"{task['task_id']}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")

    def update_task(self, task_id, new_data):

        for task in self.tasks:
            if task["task_id"] == task_id:
                task.update(new_data)
                print("Updated task")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["task_id"] != task_id]
        print("Successfully deleted task")

    def filter_tasks(self, status):
        return [task for task in self.tasks if task["status"] == status]

    def save_tasks(self):
        self.file_handler.save_tasks(self.tasks)
        print("Saved tasks")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []
























print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")

file_name = input("Enter where you want to save the tasks: ")
Tasks_management(file_name)
manager = Tasks_management(file_name)

while True:
    choice = int(input("choose an option: "))
    if choice == 1:
      task_id = input("Enter task id: ")
      title = input("Enter task title: ")
      description = input("Enter task description: ")
      due_date = input("Enter task due date: ")
      status = input("Enter task status: ")
      manager.add_task(Tasks(task_id, title, description, due_date, status))

    elif choice == "2":
      manager.view_tasks()

    elif choice == "3":
        task_id = input("Enter Task ID to update: ")
        new_title = input("Enter new title: ")
        new_status = input("Enter new status: ")
        manager.update_task(task_id, {"title": new_title, "status": new_status})

    elif choice == "4":
        task_id = input("Enter Task ID to delete: ")
        manager.delete_task(task_id)

    elif choice == "5":
        status = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered_tasks = manager.filter_tasks(status)
        for task in filtered_tasks:
            print(task)

    elif choice == "6":
        manager.save_tasks()
        print("Tasks saved successfully!")

    elif choice == "7":
        break

    else:
        print("Invalid choice! Please try again.")



