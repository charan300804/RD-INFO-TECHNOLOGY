import json
import os
import csv
from datetime import datetime, timedelta

FILENAME = "tasks.json"
PRIORITY_LEVELS = ["Low", "Medium", "High"]

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    priority = input("Set priority (Low, Medium, High): ").strip().capitalize()

    if priority not in PRIORITY_LEVELS:
        priority = "Medium"  # Default priority

    task = {
        "description": description,
        "due_date": due_date if due_date else None,
        "priority": priority,
        "completed": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\033[92mTask added successfully!\033[0m")  # Green text

# View tasks with optional filtering
def view_tasks(tasks, filter_type=None):
    today = datetime.today().date()
    print("\n\033[94m--- To-Do List ---\033[0m")  # Blue text

    filtered_tasks = []
    for task in tasks:
        due_date = task["due_date"]
        priority = task.get("priority", "Medium")
        completed = task["completed"]

        if filter_type == "completed" and not completed:
            continue
        elif filter_type == "pending" and completed:
            continue
        elif filter_type == "due_soon" and (not due_date or datetime.strptime(due_date, "%Y-%m-%d").date() > today + timedelta(days=3)):
            continue

        # Mark overdue tasks
        if due_date:
            task_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            due_status = f"(Due: {due_date})"
            if task_date < today:
                due_status += " [Overdue]"
        else:
            due_status = ""

        status = "[✔]" if completed else "[✘]"
        print(f"{status} {task['description']} {due_status} (Priority: {priority})")
        filtered_tasks.append(task)

    if not filtered_tasks:
        print("\033[91mNo tasks found.\033[0m")  # Red text

# Mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks, "pending")
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("\033[92mTask marked as completed!\033[0m")
        else:
            print("\033[91mInvalid task number.\033[0m")
    except ValueError:
        print("\033[91mInvalid input. Enter a number.\033[0m")

# Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["description"] = input("Enter new description: ").strip()
            due_date = input("Enter new due date (YYYY-MM-DD) or leave blank: ").strip()
            if due_date:
                tasks[index]["due_date"] = due_date
            priority = input("Set new priority (Low, Medium, High): ").strip().capitalize()
            if priority in PRIORITY_LEVELS:
                tasks[index]["priority"] = priority
            save_tasks(tasks)
            print("\033[92mTask updated successfully!\033[0m")
        else:
            print("\033[91mInvalid task number.\033[0m")
    except ValueError:
        print("\033[91mInvalid input. Enter a number.\033[0m")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("\033[92mTask deleted successfully!\033[0m")
        else:
            print("\033[91mInvalid task number.\033[0m")
    except ValueError:
        print("\033[91mInvalid input. Enter a number.\033[0m")

# Search tasks
def search_task(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()
    print("\n\033[94m--- Search Results ---\033[0m")
    found_tasks = [task for task in tasks if keyword in task["description"].lower()]
    
    if found_tasks:
        for task in found_tasks:
            due_status = f"(Due: {task['due_date']})" if task["due_date"] else ""
            status = "[✔]" if task["completed"] else "[✘]"
            print(f"{status} {task['description']} {due_status} (Priority: {task.get('priority', 'Medium')})")
    else:
        print("\033[91mNo tasks found matching your search.\033[0m")

# Export tasks to CSV
def export_to_csv(tasks):
    filename = "tasks_backup.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Due Date", "Priority", "Completed"])
        for task in tasks:
            writer.writerow([task["description"], task["due_date"], task["priority"], task["completed"]])
    print(f"\033[92mTasks exported to {filename} successfully!\033[0m")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n\033[96m--- To-Do List Manager ---\033[0m")  # Cyan text
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View Pending Tasks")
        print("5. View Tasks Due Soon")
        print("6. Mark Task as Completed")
        print("7. Edit Task")
        print("8. Delete Task")
        print("9. Search Task")
        print("10. Export Tasks to CSV")
        print("11. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks, "completed")
        elif choice == "4":
            view_tasks(tasks, "pending")
        elif choice == "5":
            view_tasks(tasks, "due_soon")
        elif choice == "6":
            mark_completed(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            search_task(tasks)
        elif choice == "10":
            export_to_csv(tasks)
        elif choice == "11":
            print("\033[93mExiting... Have a productive day!\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()
