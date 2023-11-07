#!/usr/bin/python3
"""Recursive script"""
import requests


def count_words(subreddit, word_list, results=None, after=None):
    """ prints a sorted count of given keywords """
    if results is None:
        results = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?'
    'limit=100&after={after}'
    # Set a custom User-Agent as recommended
    headers = {'User-Agent': '0x16-api_advanced:v1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word in title:
                    if word in results:
                        results[word] += 1
                    else:
                        results[word] = 1

        next_after = data['data']['after']
        if next_after:
            return count_words(subreddit, word_list, results, next_after)
    else:
        print("Subreddit not found or an error occurred.")
        return


# Example usage:
subreddit_name = 'python'  # Replace with the subreddit you want to check
# Replace with the keywords you want to count
keywords = ['python', 'java', 'javascript']
results = {}
count_words(subreddit_name, keywords)

# Sort the results by count (descending) and then alphabetically (ascending)
sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_results:
    print(f"{word}: {count}")
