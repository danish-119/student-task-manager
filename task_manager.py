"""Student Task Manager - a small console application."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Returns an empty list if none exist."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_tasks(tasks, path=DATA_FILE):
    """Save the task list to a JSON file."""
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(tasks, handle, indent=2)


def next_id(tasks):
    """Return the next unused task identifier."""
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(tasks, title):
    """Add a new task and return it."""
    task = {"id": next_id(tasks), "title": title, "completed": False}
    tasks.append(task)
    return task


def display_tasks(tasks):
    """Print all tasks in a simple table."""
    if not tasks:
        print("No tasks yet.")
        return
    print(f"{'ID':<4} {'Status':<8} Title")
    print("-" * 40)
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{task['id']:<4} {status:<8} {task['title']}")


def complete_task(tasks, task_id):
    """Mark the task with the given id as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return None


def delete_task(tasks, task_id):
    """Delete the task with the given id and return it.

    Raises ValueError if no task has that id; the list is left unchanged.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index)
    raise ValueError(f"Cannot delete: no task found with id {task_id}.")


def handle_add(tasks):
    title = input("Task title: ")
    task = add_task(tasks, title)
    print(f"Added task {task['id']}.")


def handle_complete(tasks):
    task_id = int(input("Task id to complete: "))
    complete_task(tasks, task_id)
    print("Done.")


def handle_delete(tasks):
    task_id = int(input("Task id to delete: "))
    delete_task(tasks, task_id)
    print("Done.")


MENU = """
Student Task Manager
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
"""


def main():
    tasks = load_tasks()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            handle_add(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            handle_complete(tasks)
        elif choice == "4":
            handle_delete(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
        save_tasks(tasks)


if __name__ == "__main__":
    main()
