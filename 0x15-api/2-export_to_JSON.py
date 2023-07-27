#!/usr/bin/python3
"""
Extending the previous task 0 to export to csv
"""
import json
import re
import requests
import sys

# defining the API url
API = "https://jsonplaceholder.typicode.com"


def main():
    """showing how many tasks is done by each user
    User id will be passed as an argument"""
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if re.fullmatch(r"\d+", sys.argv[1]):
            # getting responses
            emp_res = requests.get('{}/users/{}'.format(API, id)).json()
            emp_username = emp_res['username']
            emp_todos = requests.get(
                '{}/users/{}/todos'.format(API, id)).json()
            with open('{}.json'.format(id), 'w') as jsonfile:
                user_data = [{
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": emp_username
                } for todo in emp_todos]

                user_json = {'{}'.format(id): user_data}
                json.dump(user_json, jsonfile)


if __name__ == '__main__':
    main()
