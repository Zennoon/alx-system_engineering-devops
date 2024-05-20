#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to fetch data from the jsonplaceholder.typicode api
    about users' TODOs and print relevant information

"""
import json
import sys
from urllib import request


API_URL = "https://jsonplaceholder.typicode.com/users/{}"

if __name__ == "__main__":
    with request.urlopen(API_URL.format(sys.argv[1])) as res:
        res_body = res.read()
        employee_name = json.loads(res_body.decode("utf-8")).get("name")

    with request.urlopen((API_URL + "/todos").format(sys.argv[1])) as res:
        res_body = res.read()
        all_tasks = json.loads(res_body.decode("utf-8"))
        completed_tasks = list(filter(lambda task: task.get("completed"),
                                      all_tasks))

    output = "Employee {} is done with tasks({}/{}):"
    print(output.format(employee_name, len(completed_tasks),
                        len(all_tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
