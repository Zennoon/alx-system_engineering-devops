#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    count_words(subreddit, word_list) - Communicates with a Reddit API endpoint
    to retrieve all hot articles of a subreddit, parses their titles and prints
    a sorted count of given keywords in those titles.
"""
from requests import get


def count_words(subreddit, word_list, word_count={}, after=""):
    """
    Communicates with a Reddit API endpoint to retrieve all hot posts of
    a subreddit, parses their titles and prints a sorted count of given
    keywords in those titles.

    Args:
        subreddit (str): Name of the subreddit to extract data from
        word_list (list<str>): A list of the keywords to look for in titles
        word_count (dict): A dictionary keeping track of the count of those
                           keywords as the recursion occurs
        after (str): The string used by Reddit to navigate pagination
    """
    q_string = "?limit=100"
    if after != "":
        q_string += "&after={}".format(after)
    else:
        word_list = [word.lower() for word in word_list]
    if after is None:
        word_count = dict(sorted(word_count.items(), key=lambda x: x[0]))
        word_count = dict(sorted(word_count.items(), key=lambda x: x[1],
                                 reverse=True))
        for key, val in word_count.items():
            print("{}: {}".format(key, val))
        return
    api_url = "https://www.reddit.com/r/{}/hot.json{}".format(subreddit,
                                                              q_string)
    res = get(api_url,
              allow_redirects=False,
              headers={
                  "User-Agent": "Google Chrome Version 81.0.4044.129"
              })
    try:
        data = res.json()
    except Exception:
        return
    else:
        try:
            after = data.get("data").get("after")
            titles = [post.get("data").get("title")
                      for post in data.get("data").get("children")]
        except KeyError:
            return
        else:
            for title in titles:
                for word in title.split():
                    if word.lower() in word_list:
                        count = word_list.count(word.lower())
                        if word.lower() in word_count:
                            word_count[word.lower()] += count
                        else:
                            word_count[word.lower()] = count
    count_words(subreddit, word_list, word_count, after)
