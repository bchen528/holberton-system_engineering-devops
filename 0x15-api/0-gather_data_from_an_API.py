#!/usr/bin/python3
"""
returns information about his/her TODO list progress for a
given employee ID using a REST API
"""
import requests
from sys import argv


def get_todo():
    """returns employee's TODO list progress"""
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    r_todo_true = requests.get('https://jsonplaceholder.typicode.com/todos?'
                               'userId={}&&completed=true'.format(argv[1]))
    r_todo_false = requests.get('https://jsonplaceholder.typicode.com/todos?'
                                'userId={}&&completed=false'.format(argv[1]))
    try:
        user_dict = r_user.json()
        true_todo_dict = r_todo_true.json()
        false_todo_dict = r_todo_false.json()
        print("Employee {} is done with tasks({}/{}):".
              format(user_dict['name'], len(true_todo_dict),
                     len(false_todo_dict) + len(true_todo_dict)))
        for task in true_todo_dict:
            print("\t {}".format(task['title']))
    except:
        pass
if __name__ == "__main__":
    get_todo()
