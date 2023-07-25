#!/usr/bin/python3
""" Python script that,for a given employee ID, returns info
about his/her TODO list progress using JSONPlaceholder API """
import requests
import sys

def get_employee_name(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    try:
        response = requests.get(user_url)
        response.raise_for_status()
        user_info = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch user information - {e}")
        return

    return user_info.get('name', 'Unknown Employee')

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data - {e}")
        return

    # Count completed tasks and total tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)

    # Get employee name
    employee_name = get_employee_name(employee_id)

    # Display the result in the required format
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print("\t", task['title'])

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide an integer.")

