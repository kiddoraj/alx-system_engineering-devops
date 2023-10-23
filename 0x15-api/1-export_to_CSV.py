#!/usr/bin/python3
"""
Module to fetch employee TODO list progress and export it to a CSV file.
"""

import csv
import requests
import sys


def fetch_todo_list(employee_id):
    """
    Fetch employee TODO list progress and export it to a CSV file.

    Args:
        employee_id (int): The employee ID to fetch information for.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if (user_response.status_code != 200 or
                todo_response.status_code != 200):
            print("Error: Unable to fetch data from the API.")
            return

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data["username"]

        # Prepare CSV file name based on USER_ID
        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write CSV header
            csv_writer.writerow([
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ])

            for task in todo_data:
                task_completed = "Yes" if task["completed"] else "No"
                csv_writer.writerow([
                    user_data["id"],
                    employee_name,
                    task_completed,
                    task["title"]
                ])

        print(f"Employee {employee_name}'s tasks have"
              "been exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
