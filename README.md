# Task Manager

This is a Python script for managing tasks and users. It provides various functionalities such as registering new users, adding tasks, marking tasks as complete, editing tasks, and generating reports based on task completion and overdue tasks.

## Getting Started

To run the script, you need to have Python installed on your machine. Follow these steps:

1. Clone the repository or download the script file.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the following command to execute the script:
   ```
   python task_manager.py
   ```

## Dependencies

This script requires the following dependencies:

- Python 3.x

## Functionality

The script provides the following functionality:

1. Register new users: Only users with the "admin" username can register new users.
2. Add tasks: Add new tasks with assigned users, task title, description, and due date.
3. View all tasks: Display all tasks with detailed information.
4. View my tasks: Display tasks assigned to the current user.
5. Mark task as complete: Mark a task as complete based on the task number.
6. Edit task: Edit task details such as username or due date based on the task number.
7. Generate reports:
   - Percentage of completed tasks per user.
   - Number of tasks completed and not completed per user.
   - Number of tasks overdue per user.
   - Number of tasks that are overdue and not completed.
8. Exit: Exit the script.

## Usage

When running the script, you will be prompted to enter your username and password. The script will authenticate the user and provide a menu with options for different actions. Choose the desired option by entering the corresponding number.

**Use username: 'admin' and password: adm1n to get started.**

Please note that the script reads user credentials from the "user.txt" file and tasks from the "tasks.txt" file. Make sure these files exist and have the appropriate format.

## File Structure

The script consists of the following files:

- `task_manager.py`: The main script file containing the task management functionality.
- `user.txt`: A text file storing user credentials in the format `username, password`.
- `tasks.txt`: A text file storing task details in the format `username, task_title, task_description, date_assigned, due_date, complete_status`.

Enjoy using the Task Manager! If you have any questions, please don't hesitate to contact me.
