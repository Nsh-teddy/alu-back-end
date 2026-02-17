#!/usr/bin/python3
"""
Export all tasks of a given employee to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get employee info
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Failed to get user info")
        sys.exit(1)
    user_data = response_user.json()
    username = user_data.get("username")

    # Get TODO list
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print("Failed to get todos")
        sys.exit(1)
    todos = response_todos.json()

    # CSV file name
    csv_filename = "{}.csv".format(employee_id)

    # Write CSV
    with open(csv_filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
