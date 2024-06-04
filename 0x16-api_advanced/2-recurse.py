#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    recurse(subreddit, hot_list=[]) - Returns a list of all the hot posts'
    titles in a given subreddit. It operates recursively
"""
from requests import get


def recurse(subreddit, hot_list=[]):
    """
    Returns a list of all the hot posts' titles in a given subreddit.
    It operates recursively.

    Args:
        subreddit (str): Name of the subreddit to operate on
        hot_list (list<str>): List to hold the titles

    Returns:
        list<str>: hot_list
    """
    if subreddit is None or not isinstance(subreddit, str):
        return (None)
    if len(hot_list) == 0:
        after = ""
        q_string = ""
    else:
        after = hot_list[0]
        q_string = "&after={}".format(after)
    if after is None:
        return (hot_list[1:])
    api_url = "https://www.reddit.com/r/{}/hot.json?limit=100{}"
    res = get(api_url.format(subreddit,
                             q_string),
              allow_redirects=False,
              headers={
                  "User-Agent": "Google Chrome Version 81.0.4044.129"
              })
    try:
        data = res.json()
    except Exception as e:
        return (None)
    else:
        try:
            if len(hot_list) == 0:
                hot_list.append(data.get("data").get("after"))
            else:
                hot_list[0] = data.get("data").get("after")
            hot_list.extend([post["data"]["title"]
                             for post in data["data"]["children"]])
        except KeyError as e:
            return (None)
    return (recurse(subreddit, hot_list))
