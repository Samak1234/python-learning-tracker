# ============================================================
# Project  : Python Learning Tracker (CLI)
# File     : learning_tracker.py
# Author   : Samaksh
# Version  : 1.3 - Day 4 (JSON File Persistence)
# ============================================================
# Description:
#   A command-line based personal learning tracker built in Python.
#   This project is being developed incrementally over 4 weeks,
#   starting from core Python fundamentals and scaling up to
#   OOP, file handling, SQLite, REST APIs, and ML integration.
#
# Current Version Features:
#   - Add new tasks via CLI
#   - View tasks with numbering
#   - Delete tasks by selecting index
#   - Persist tasks using a JSON file
#   - Load saved tasks automatically when the program starts
#   - Modular structure using functions
#   - Centralized program flow using main() entry point
#
# Concepts Used:
#   - Variables, Strings, Lists
#   - Loops (for, while)
#   - Conditionals (if/elif/else)
#   - Functions (def)
#   - File handling
#   - JSON serialization/deserialization
#   - List methods (append, pop)
#   - User input handling
#   - Basic program structuring (main function, entry point)
#   - Exception handling with try/except
# ============================================================

"""
Simple CLI-based Task Manager.

Features:
- Add tasks
- View tasks with numbering
- Delete a task by number
- Save tasks permanently using JSON
- Load saved tasks automatically on startup
- Exit program

Concepts used:
- Lists
- Loops
- Conditionals
- Functions
- File handling
- JSON
- User input handling
- Exception handling
"""

# Helps convert tasks between Python list ↔ file format (JSON)
import json

def load_tasks():
    """Load tasks from file. Return empty list if file doesn't exist."""
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks():
    """Save current tasks to file so data persists after program ends."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Load tasks from file (or start with empty list if none exist)
tasks = load_tasks()


def add_task():
    """Prompt the user to enter a task and add it to the list."""
    task = input("Enter a task: ")
    tasks.append(task)  # Add task to the list
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    """Display all tasks with their index numbers."""
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        # Loop through tasks using index to display numbering
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")  # Print task number (starting from 1) and the task


def delete_task():
    """Show all tasks and allow user to delete one by number."""
    view_tasks()  # Show current tasks before asking which to delete

    if len(tasks) == 0:
        print("No tasks to delete!")
        return  # Nothing to delete, exit function early

    index = int(input("Enter task number to delete: ")) - 1  # Convert to 0-based index
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)  # Remove task at given index and store it
        print("Removed:", removed)
    else:
        print("Invalid number")  # User entered a number outside the valid range


def main():
    """Main loop that keeps the program running and handles menu navigation."""

    # Infinite loop to keep the program running until user exits
    while True:

        # Display menu options to the user
        print("\n------ TASK MANAGER ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        # Take user input (always comes as string)
        choice = input("Enter your choice: ")

        # Option 1: Add a new task
        if choice == "1":
            add_task()

        # Option 2: View all tasks
        elif choice == "2":
            view_tasks()

        # Option 3: Delete a task
        elif choice == "3":
            delete_task()

        # Option 4: Exit program
        elif choice == "4":
            print("Exiting program...")
            break  # Stops the infinite loop and ends the program

        # Handle invalid input
        else:
            print("Invalid choice. Try again.")


# Entry point — only runs main() if this file is executed directly
# (not when imported as a module into another file)
if __name__ == "__main__":
    main()