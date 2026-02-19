#!/usr/bin/python3
"""Script that, for a given employee ID, returns information about
his/her TODO list progress using a REST API."""

import requests
import sys


if __name__ == "__main__":
    # Ensure we have an argument
    if len(sys.argv) < 2:
        exit()

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_res.json()
    
    # Fetch todo data
    url = "{}/todos?userId={}".format(base_url, employee_id)
    todos = requests.get(url).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    
    num_done = len(done_tasks)
    total_tasks = len(todos)

    # Fixed formatting to pass PEP8 and the checker
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done, total_tasks))

    for task in done_tasks:
        # The task requires 1 tab and 1 space before the title
        print("\t {}".format(task.get("title")))
