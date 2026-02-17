#!/usr/bin/python3
"""Script that, for a given employee ID, returns information about
his/her TODO list progress using a REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(
        base_url, employee_id)).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
