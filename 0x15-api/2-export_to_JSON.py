#!/usr/bin/python3
"""
returns information about his/her TODO list progress for a
given employee ID using a REST API and export data in the JSON format
"""
import json
import requests
from sys import argv


def get_todo_json():
    """returns employee's TODO list progress"""
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    r_todo = requests.get('https://jsonplaceholder.typicode.com/todos?'
                          'userId={}'.format(argv[1]))
    try:
        user_dict = r_user.json()
        task_dict = r_todo.json()
        data = {}
        data['{}'.format(user_dict["id"])] = []
        for task in task_dict:
            data['{}'.format(user_dict["id"])].append({
                "task": '{}'.format(task["title"]),
                "completed": '{}'.format(task["completed"]),
                "username": '{}'.format(user_dict["username"])
            })
        with open("{}.json".format(argv[1]), "w") as jsonfile:
            json.dump(data, jsonfile)
            '''
            for task in task_dict:
                f.writerow([user_dict["id"], user_dict["username"],
            task["completed"], task["title"]])
            '''
    except:
        pass
if __name__ == "__main__":
    get_todo_json()
