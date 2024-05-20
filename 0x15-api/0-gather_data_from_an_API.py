#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to fetch data from the jsonplaceholder.typicode api
    about users' TODOs and print relevant information

"""
import sys
import requests


if __name__ == "__main__":
    ARGV = sys.argv
    API_URL = "https://jsonplaceholder.typicode.com/users/{}".format(ARGV[1])
    employee_res = requests.get(API_URL).json()
    employee_name = employee_res.get("name")

    tasks_res = requests.get(API_URL + "/todos").json()

    completed_tasks = list(filter(lambda task: task.get("completed"),
                                  tasks_res))

    output = "Employee {} is done with tasks({}/{}):"
    print(output.format(employee_name, len(completed_tasks),
                        len(tasks_res)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
