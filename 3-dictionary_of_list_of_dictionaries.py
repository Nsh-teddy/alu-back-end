#!/usr/bin/python3
import json
import requests
import sys

# API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch users
users = requests.get(users_url).json()
todos = requests.get(todos_url).json()

# Build a dictionary of all employees
all_data = {}
for user in users:
    user_id = str(user['id'])
    username = user['username']
    user_tasks = []
    for todo in todos:
        if todo['userId'] == user['id']:
            task_dict = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task_dict)
    all_data[user_id] = user_tasks

# Save to JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(all_data, f)
