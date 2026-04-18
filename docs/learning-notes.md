# 📘 Python Learning Notes


## Day 4: JSON & File Persistence
What are “JSON tools”?

JSON tools = functions provided by Python’s json module

They help you:

convert data between Python and JSON format
### What is JSON?

JSON (JavaScript Object Notation) is a lightweight data format used to store and exchange data.
It is just a text format to store data
It looks like a Python dictionary:

Example:
```json
["Learn Python", "Practice loops"]

🔹 Problem (why we need JSON tools)

Python uses:

tasks = ["Learn Python", "Build project"]

File uses:

["Learn Python", "Build project"]

 They look similar, but Python cannot directly understand file text.

 JSON tools = Translator

They convert:

Direction	Tool
File → Python	json.load()
Python → File	json.dump()

1. json.load()
tasks = json.load(file)
Super simple

Read JSON file → convert to Python list

Technical

Deserializes JSON data from a file object into a Python object.

Example

File:

["A", "B", "C"]

Becomes:

["A", "B", "C"]



 2. json.dump()


json.dump(tasks, file)
Super simple

Take Python list → save it into file as JSON

Technical

Serializes a Python object into JSON format and writes it to a file.

Example

Python:

tasks = ["A", "B", "C"]

Saved as:

["A", "B", "C"]


Real-life analogy

Situation	Meaning
json.load()	Reading a notebook
json.dump()	Writing into notebook