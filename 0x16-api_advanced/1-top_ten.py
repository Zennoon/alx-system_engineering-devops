#!/usr/bin/python3
"""

Contains:
    Functions
    =========
    top_ten(subreddit) - Communicates with a reddit API endpoint and retrieves
    the title of the top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Communicates with a reddit API endpoint and prints the title of
    the top ten posts of a given subreddit

    Args:
        subreddit (str): Name of the subreddit whose top ten posts' titles
        are printed
    """
    endpoint_api = "https://www.reddit.com/r/{}/top.json?limit=10"
    res = requests.get(endpoint_api.format(subreddit),
                       allow_redirects=False,
                       headers={
                           "User-Agent": "top-ten-subreddit-posts"
                       })
    data = res.json()
    if data.get("data") is not None:
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
