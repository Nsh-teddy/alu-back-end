#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check if employee ID was given
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Get employee info
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)
    employee = response_user.json()
    employee_name = employee.get("name")

    # Get TODO list
    response_todos = requests.get(todos_url)
    todos = response_todos.json()

    # Count completed tasks
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(completed_tasks)

    # Print first line
    print("Employee {} is done with tasks({}/{}):".format(employee_name, number_done, total_tasks))

    # Print completed tasks with 1 tab + 1 space
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
