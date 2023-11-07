#!/usr/bin/python3
"""Prints The titles of first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Prints the titles of first 10 hot posts"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    # Set a custom User-Agent as recommended
    headers = {'User-Agent': '0x16-api_advanced:v1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            print(f"No hot posts found in r/{subreddit}.")
        else:
            print(f"Top 10 hot posts in r/{subreddit}:\n")
            for i, post in enumerate(posts, start=1):
                title = post['data']['title']
                print(f"{i}. {title}")
    else:
        print("None")  # Invalid subreddit or other error
