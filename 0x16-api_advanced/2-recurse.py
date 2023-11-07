#!/usr/bin/python3
"""Recursive script"""

import requests
import sys


def recurse(subreddit, hot_list=None, after=None, count=0):
    """returns a list containing the titles """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Set a custom User-Agent as recommended
    headers = {'User-Agent': '0x16-api_advanced:v1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get('data', {})

    # Extract the "after" and "children" fields from the data
    after = data.get('after')
    children = data.get('children', [])

    # Extract titles and add them to the hot_list
    hot_list.extend(post['data']['title'] for post in children)

    if after:
        # Recursive call with the 'after' parameter to fetch the next page
        return recurse(subreddit, hot_list, after, count + len(children))
    else:
        return hot_list


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 2-main.py <subreddit>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    hot_titles = recurse(subreddit_name)

    if hot_titles is not None:
        print(f"Titles of hot articles in r/{subreddit_name}:\n")
        for i, title in enumerate(hot_titles, start=1):
            print(f"{i}. {title}")
    else:
        print("None")
