# ============================================================
# Project  : Python Learning Tracker (CLI)
# File     : learning_tracker.py
# Author   : Samaksh
# Version  : 1.0 - Day 1 (Foundation)
# ============================================================
# Description:
#   A command-line based personal learning tracker built in Python.
#   This project is being developed incrementally over 4 weeks,
#   starting from core Python fundamentals and scaling up to
#   OOP, file handling, SQLite, REST APIs, and ML integration.
#
# Current Version Features:
#   - Accept multiple learning tasks from the user via CLI
#   - Store tasks in a Python list (in-memory)
#   - Display all entered tasks in a formatted list
#
# Concepts Used:
#   - Variables, Strings, Lists
#   - for loop, range()
#   - input(), print()
#   - list.append()
# ============================================================

"""
Simple CLI-based Task Manager.

Features:
- Add tasks
- View tasks with numbering
- Exit program

Concepts used:
- Lists
- Loops
- Conditionals
- User input handling
"""


# List to store all tasks entered by the user
tasks = []
# Infinite loop to keep the program running until user exits
while True:

    #display menu options to the user
    print("\n------ TASK MANAGER ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    #Take user input(always come as string)
    choice = input("Enter your choice: ")

    #option 1: Add a new task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)#add task to the list 

    
    #option 2:View all tasks
    elif choice == "2":
        print("\nYour tasks:")
        #check if task list is empty 
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            #loop through tasks using index to display numbering
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")#Print task number (starting from 1) and the task from the list
    
    # Option 3: Exit program
    elif choice == "3":
        print("Exiting program...")
        break # stops the infinite loop and ends program

    # Handle invalid input
    else:
        print("Invalid choice. Try again.")
        