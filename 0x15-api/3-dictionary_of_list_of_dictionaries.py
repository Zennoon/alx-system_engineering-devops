#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to fetch data from the jsonplaceholder.typicode api
    about all users and their TODOs and stores relevant info to
    a file in JSON format

"""
import json
import requests


if __name__ == "__main__":
    USERS_URL = "https://jsonplaceholder.typicode.com/users"

    output = {}
    all_users = requests.get(USERS_URL).json()
    for user in all_users:
        tasks_url = USERS_URL + "/{}/todos".format(user.get("id"))
        tasks = requests.get(tasks_url).json()
        output[user.get("id")] = [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed"),
        } for task in tasks]

    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        json.dump(output, f)
