#!/usr/bin/python3
"""Export employee's tasks to JSON"""

import json
import requests
import sys

# Check if user provided an employee ID
if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# URLs to fetch employee and tasks
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

# Get employee info
response_user = requests.get(user_url)
employee = response_user.json()
username = employee.get("username")

# Get employee tasks
response_todos = requests.get(todos_url)
todos = response_todos.json()

# Prepare JSON data
data = {employee_id: []}
for task in todos:
    data[employee_id].append({
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    })

# Write JSON to file named USER_ID.json
filename = "{}.json".format(employee_id)
with open(filename, "w") as json_file:
    json.dump(data, json_file)
