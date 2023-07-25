#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress using a REST API and export the data in CSV format.
"""

import requests
import csv

def get_employee_name(employee_id):
    """
    Fetches the name of the employee from the user information.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    try:
        response = requests.get(user_url)
        response.raise_for_status()
        user_info = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch user information - {e}")
        return "Unknown Employee"

    return user_info.get('name', 'Unknown Employee')

def get_employee_todo_progress(employee_id):
    """
    Fetches employee's TODO list progress and displays it in the specified format.
    Exports the data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data - {e}")
        return

    # Get employee name
    employee_name = get_employee_name(employee_id)

    # Prepare the data for CSV export
    csv_data = []
    for task in todos:
        csv_data.append([employee_id, employee_name, task['completed'], task['title']])

    # Export data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)

    print(f"CSV data exported to {filename}.")

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

