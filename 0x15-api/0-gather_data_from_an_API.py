#!/usr/bin/python3
"""
Module to fetch and display employee TODO list progress using a REST API.
"""

import sys
import requests

def fetch_todo_list(employee_id):
    """
    Fetch and display employee TODO list progress.

    Args:
        employee_id (int): The employee ID to fetch information for.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if user_response.status_code != 200 or todo_response.status_code != 200:
            print("Error: Unable to fetch data from the API.")
            return

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data["name"]
        total_tasks = len(todo_data)
        done_tasks = [task for task in todo_data if task["completed"]]

        print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)

