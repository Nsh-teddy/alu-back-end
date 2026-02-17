#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches TODO list of an employee from a REST API and prints completed tasks
"""

import requests
import sys


def main():
    """Fetches employee data and prints completed tasks."""

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    employee_id = sys.argv[1]

    # URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    # Get user info
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Failed to fetch user data")
        return
    employee_name = response_user.json().get("name")

    # Get TODO list
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print("Failed to fetch todos")
        return
    todos = response_todos.json()

    # Count completed tasks
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(completed_tasks)

    # Print first line
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_done, total_tasks
        )
    )

    # Print completed tasks with 1 tab + 1 space
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
