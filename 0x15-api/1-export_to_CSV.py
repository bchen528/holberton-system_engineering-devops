#!/usr/bin/python3
"""
returns information about his/her TODO list progress for a
given employee ID using a REST API
"""
import csv
import requests
from sys import argv


def get_todo_csv():
    """returns employee's TODO list progress"""
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    r_todo = requests.get('https://jsonplaceholder.typicode.com/todos?'
                          'userId={}'.format(argv[1]))
    try:
        user_dict = r_user.json()
        task_dict = r_todo.json()
        with open("{}.csv".format(argv[1]), "w") as csvfile:
            f = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            for task in task_dict:
                f.writerow([user_dict["id"], user_dict["username"],
                            task["completed"], task["title"]])
    except:
        pass
if __name__ == "__main__":
    get_todo_csv()
