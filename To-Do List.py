import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            if isinstance(tasks, list):
                return tasks
            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for idx, task in enumerate(tasks, 1):
        title = task.get("title", "Untitled task")
        status = "✔" if task.get("done") else "❌"
        print(f"{idx}. [{status}] {title}")


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        idx = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid integer.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        idx = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Deleted task: '{removed.get('title', 'Untitled task')}'")
        else:
            print("Task does not exist.")
    except ValueError:
        print("Please enter a valid integer.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- MENU ---")
        print("1. View Tasks\n2. Add Task\n3. Mark Task Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()