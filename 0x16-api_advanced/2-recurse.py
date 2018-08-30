#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, return None
"""
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles
    for a given subreddit"""
    try:
        if after is None:
            r_before = get('http://www.reddit.com/r/{}/hot.json?limit=100'.
                           format(subreddit, after),
                           headers={'User-Agent': 'bc'})
            subreddit_dict = r_before.json()
        else:
            r_after = get('https://www.reddit.com/r/{}/hot.json?limit=100&&'
                          'after={}'.format(subreddit, after),
                          headers={'User-Agent': 'bc'})
            subreddit_dict = r_after.json()

        for i in range(len(subreddit_dict['data']['children'])):
            hot_list.append(subreddit_dict['data']['children'][i]
                            ['data']['title'])

        after = subreddit_dict['data']['after']

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except:
        return None
