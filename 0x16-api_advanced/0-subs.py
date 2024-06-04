#!/usr/bin/python3
"""

Contains:
    Functions
    =========
    number_of_subscribers(subreddit) - Communicates with the Reddit API to get
    the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Communicates with the Reddit API to get the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit whose subscribers count
        is extracted

    Returns:
        int: The number of subscribers of the given subreddit (0 if the
        subreddit doesn't exist)
    """
    num_subscribers = 0
    endpoint_url = "https://www.reddit.com/r/{}/about.json"
    res = requests.get(endpoint_url.format(subreddit),
                       allow_redirects=False,
                       headers={
        "User-Agent": "number-of-subscribers"
    })
    data = res.json()
    if data.get("data") is not None:
        num_subscribers = data["data"]["subscribers"]
    return (num_subscribers)


print(number_of_subscribers("programming"))
print(number_of_subscribers("this_shouldn't_exist_zennoon"))
