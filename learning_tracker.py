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

tasks = []

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3. Exit")

    choice = input("Enter your choices: ")

    if choice =="1":
        task=input("Enter a task:")
        tasks.append(task)
    
    elif choice=="2":
        print("\n Your tasks:")
        for item in tasks:
            print("-",item)
    
    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.Try again")
        