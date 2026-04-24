# ============================================================
# Project  : Python Learning Tracker (CLI)
# File     : learning_tracker.py
# Author   : Samaksh
# Version  : 1.4 - Day 6 (Task Metadata + Mark Done + Validation)
# ============================================================
# Description:
#   A command-line based personal learning tracker built in Python.
#   The project is evolving step-by-step from basic Python concepts
#   to a more structured and real-world application.

# Current Version Features:
#   - Add tasks with metadata (title, status, created time)
#   - View tasks with numbering, status, and timestamp
#   - Delete tasks by selecting index
#   - Persist tasks using a JSON file
#   - Load saved tasks automatically on startup
#   - Backward compatibility for old task format (string → object)
#   - Modular structure using functions
#   - Centralized program flow using main()
#   - Mark tasks as done (✔ / ❌ status display)
#   - Input validation with specific ValueError handling
#   - Fixed view_tasks indentation bug
#   - JSON saved with indent=4 for readability

# Concepts Used:
#   - Lists of dictionaries (structured data)
#   - Loops (for, while)
#   - Conditionals (if/elif/else)
#   - Functions (def)
#   - File handling
#   - JSON serialization/deserialization
#   - Date & time handling (datetime)
#   - Exception handling (try/except)
# ============================================================

"""
CLI-based Task Manager with structured task storage.

Features:
- Add tasks with status and timestamp
- View tasks with numbering and status (✔ / ❌)
- Delete tasks by number
- Save tasks using JSON (persistent storage)
- Load tasks automatically on startup
- Handles old data format safely

Concepts used:
- Lists & Dictionaries
- Loops & Conditionals
- Functions
- File handling (JSON)
- Datetime module
- Exception handling
"""

from datetime import datetime # Import datetime class to handle and format task creation timestamps
# Helps convert tasks between Python list ↔ file format (JSON)
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

            # If old format (list of strings), convert to new structured format
            if len(data) > 0 and isinstance(data[0], str):
                new_data = []
                for item in data:
                    new_data.append({
                        "title": item,
                        "done": False,
                        "created_at": "unknown"
                    })
                return new_data

            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or error occurs, return empty list
        return []


def save_tasks():
    """Save current tasks to file so data persists after program ends."""
    with open("tasks.json", "w") as file:
        json.dump(tasks,file, indent=4) # indent=4 makes the file neat and readable

# Load tasks from file (or start with empty list if none exist)
tasks = load_tasks()


def add_task():
    """Prompt the user to enter a task and add it to the list."""
    task = input("Enter a task: ")
    # Create structured task object instead of plain string
    task_obj = {
    "title": task,
    "done": False, # Task is initially not completed
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M") # Store timestamp
    }
    tasks.append(task_obj)
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
            task = tasks[i]
            status = "✔" if task["done"] else "❌"
            print(f"{i + 1}. {task['title']} [{status}] ({task['created_at']})")


def delete_task():
    """Show all tasks and allow user to delete one by number."""
    

    if len(tasks) == 0:
        print("No tasks to delete!")
        return  # Nothing to delete, exit function early

    view_tasks()  # Show current tasks before asking which to delete

    try:
        index = int(input("Enter task number to delete: ")) - 1  # Convert to 0-based index
    except ValueError:
        print("Please enter a valid number!")
        return 

    if 0 <= index < len(tasks):
        # Remove task using index and show only the title
        removed = tasks.pop(index)  # Remove task at given index and store it
        print("Removed:", removed["title"])
    else:
        print(f"Enter a number between 1 and {len(tasks)}")  # User entered a number outside the valid range

def mark_done():
    """Let user mark a task as completed."""
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number to mark done: ")) - 1
    except ValueError:
        print("Please enter a valid number!")
        return

    if 0 <= index < len(tasks):
        tasks[index]["done"] = True   # flip done from False to True
        save_tasks()
        print(f"✔ '{tasks[index]['title']}' marked as done!")
    else:
        print(f"Enter a number between 1 and {len(tasks)}")

def main():
    """Main loop that keeps the program running and handles menu navigation."""

    # Infinite loop to keep the program running until user exits
    while True:

        # Display menu options to the user
        print("\n------ TASK MANAGER ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Done")
        print("5. Exit")

        # Take user input (always comes as string)
        choice = input("Enter your choice: ")
        
        if choice not in ["1", "2", "3", "4","5"]:
            print("Invalid choice. Try again.")
            continue
        # Option 1: Add a new task
        if choice == "1":
            add_task()

        # Option 2: View all tasks
        elif choice == "2":
            view_tasks()

        # Option 3: Delete a task
        elif choice == "3":
            delete_task()

        elif choice == "4":
            mark_done()

        elif choice == "5":
            print("Exiting...")
            break
        
# Entry point — only runs main() if this file is executed directly
# (not when imported as a module into another file)
if __name__ == "__main__":
    main()