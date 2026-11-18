# Student Task Manager - User Guide

## Starting the program

Open a terminal in the project folder and run:

```bash
python task_manager.py
```

Your tasks are loaded from `tasks.json` (created automatically on first use)
and saved after every action.

## Menu options

| Option | What it does |
| ------ | ------------ |
| 1. Add task | Asks for a title and adds a new pending task. |
| 2. Show tasks | Lists every task with its id, status and title. |
| 3. Complete task | Asks for a task id and marks that task as completed. |
| 4. Delete task | Asks for a task id and removes that task. |
| 5. Exit | Saves and closes the program. |

## Reading the task list

```
ID   Status   Title
----------------------------------------
1    [x]      Read chapter 3
2    [ ]      Write lab report
```

`[ ]` means the task is still pending and `[x]` means it is completed.

## Rules and messages

- A task title cannot be empty or contain only spaces:
  `Could not add task: Task title cannot be empty.`
- A title can have at most 100 characters.
- Completing a task that is already completed, or an id that does not exist,
  shows `Could not complete task: ...` and changes nothing.
- Deleting needs a valid positive number that matches an existing task.
  Otherwise you see `Could not delete task: ...` and no task is removed.

## Tips

- Use option 2 first to see the ids of your tasks.
- Task ids are never reused while a larger id exists, so an id always points to one task.
- To start fresh, delete the `tasks.json` file.

## Running the tests

```bash
python -m unittest discover -s tests -v
```
