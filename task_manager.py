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
