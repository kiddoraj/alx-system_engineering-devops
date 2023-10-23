#!/usr/bin/python3
"""
Module to fetch and export all employees' TODO list progress to a JSON file.
"""

import json
import requests


def fetch_and_export_all_employees():
    """
    Fetch and export all employees' TODO list progress to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users"
    all_data = {}

    try:
        user_response = requests.get(user_url)

        if user_response.status_code != 200:
            print("Error: Unable to fetch data from the API.")
            return

        user_data = user_response.json()

        for user in user_data:
            employee_id = user["id"]
            employee_name = user["username"]
            todo_url = f"{base_url}/todos?userId={employee_id}"
            todo_response = requests.get(todo_url)

            if todo_response.status_code == 200:
                todo_data = todo_response.json()
                tasks = [{"username": employee_name,
                          "task": task["title"],
                          "completed": task["completed"]}
                         for task in todo_data]
                all_data[employee_id] = tasks

        # Prepare JSON file name
        json_filename = "todo_all_employees.json"

        with open(json_filename, 'w') as json_file:
            json.dump(all_data, json_file, indent=4)

        print(
            "Data for all employees' tasks has "
            f"been exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == "__main__":
    fetch_and_export_all_employees()
