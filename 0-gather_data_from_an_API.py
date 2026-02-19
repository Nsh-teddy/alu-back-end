#!/usr/bin/python3
"""
Script that, for a given employee ID, returns information about
his/her TODO list progress using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    # Get employee ID from the first command line argument
    if len(sys.argv) < 2:
        exit()

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # 1. Fetch User data
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_res = requests.get(user_url)
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # 2. Fetch TODO list data
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)
    todo_res = requests.get(todo_url)
    todos = todo_res.json()

    # 3. Process the tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    num_done = len(done_tasks)

    # 4. Print the header
    # We keep the format call on one line or clean breaks to avoid W503
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done, total_tasks))

    # 5. Print the completed tasks with 1 tab and 1 space
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
