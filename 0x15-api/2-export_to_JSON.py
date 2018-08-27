#!/usr/bin/python3
"""
returns information about his/her TODO list progress for a
given employee ID using a REST API and export data in the JSON format
"""
from sys import argv
import json
from collections import OrderedDict
import requests


def get_todo_json():
    """returns employee's TODO list progress"""
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    r_todo = requests.get('https://jsonplaceholder.typicode.com/todos?'
                          'userId={}'.format(argv[1]))
    try:
        user_dict = r_user.json()
        task_list = r_todo.json()
        data = {}
        data['{}'.format(user_dict["id"])] = []
        for task in task_list:
            a_dict = OrderedDict()
            a_dict["task"] = task["title"]
            a_dict["completed"] = task["completed"]
            a_dict["username"] = user_dict["username"]
            data['{}'.format(user_dict["id"])].append(a_dict)
        with open("{}.json".format(argv[1]), "w") as jsonfile:
            json.dump(data, jsonfile)
    except:
        pass

if __name__ == "__main__":
    get_todo_json()
