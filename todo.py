def display_tasks(tasks):
    """Display all tasks in the dictionary."""
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\n--- To-Do List ---")
    for task_id, details in tasks.items():
        print(f"ID: {task_id} | Task: {details['task']} | Status: {details['status']}")
    print()

def add_task(tasks, task_id_counter):
    """Add a new task."""
    task_name = input("Enter task description: ").strip()
    if not task_name:
        print("Task description cannot be empty.")
        return task_id_counter
    tasks[task_id_counter] = {"task": task_name, "status": "Pending"}
    print(f"Task '{task_name}' added successfully!")
    return task_id_counter + 1


def update_task_status(tasks):
    """Update the status of an existing task."""
    try:
        task_id = int(input("Enter task ID to update: "))
        if task_id not in tasks:
            print("Task ID not found.")
            return
        new_status = input("Enter new status (Pending/Done): ").strip().capitalize()
        if new_status not in ["Pending", "Done"]:
            print("Invalid status. Use 'Pending' or 'Done'.")
            return
        tasks[task_id]["status"] = new_status
        print("Task status updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")


def delete_task(tasks):
    """Delete a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
        if task_id in tasks:
            deleted_task = tasks.pop(task_id)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")


def main():
    tasks = {}  # Dictionary to store tasks
    task_id_counter = 1  # Unique ID for each task

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task_id_counter = add_task(tasks, task_id_counter)
        elif choice == "3":
            update_task_status(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()