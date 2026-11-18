# Student Task Manager

![Tests](https://github.com/danish-119/student-task-manager/actions/workflows/tests.yml/badge.svg)

A small Python console application for students to keep track of their tasks.
Tasks are stored in a local `tasks.json` file, so they are still there the next
time you start the program.

Project status: In Development (release v1.0.0 is ready)

## Features

- Add tasks (empty or whitespace-only titles are rejected, titles are limited to 100 characters)
- Display all tasks with their id and status (`[ ]` pending, `[x]` completed)
- Mark a selected task as completed (unknown ids and repeated completion are reported)
- Delete a task by its identifier (invalid ids are rejected and nothing is removed)
- Automatic saving to `tasks.json`
- Unit tests and a GitHub Actions workflow

## Setup

Requirements: Python 3.8 or newer. There are no third-party dependencies.

```bash
git clone https://github.com/danish-119/student-task-manager.git
cd student-task-manager
```

## Usage

Start the program from the project folder:

```bash
python task_manager.py
```

Choose an option from the menu:

```
Student Task Manager
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

Example session:

```
Choose an option: 1
Task title: Finish DevOps lab
Added task 1: Finish DevOps lab
Choose an option: 3
Task id to complete: 1
Completed task 1: Finish DevOps lab
```

See the [user guide](docs/user-guide.md) for more details.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically on GitHub Actions for every push to `main`
and for every pull request to `main`.

## Project layout

```
task_manager.py          the application
tests/                   unittest test suite
docs/user-guide.md       short user guide
docs/assignment-report.md  explanations and evidence for the lab assignment
.github/workflows/       GitHub Actions workflow
```

## License

Released under the [MIT License](LICENSE).
