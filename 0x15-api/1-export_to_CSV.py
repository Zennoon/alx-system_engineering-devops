#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to fetch data from the jsonplaceholder.typicode api
    about users' TODOs and store relevant information in csv
    format to a file

"""
import requests
import sys


if __name__ == "__main__":
    ARGV = sys.argv
    user_id = ARGV[1]
    API_URL = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    employee_res = requests.get(API_URL).json()
    employee_username = employee_res.get("username")

    tasks_res = requests.get(API_URL + "/todos").json()

    with open("{}.csv".format(ARGV[1]), 'w', encoding="utf-8") as f:
        for task in tasks_res:
            f.write('"{}","{}","{}","{}"\n'.format(user_id, employee_username,
                                                   task.get("completed"),
                                                   task.get("title")))
