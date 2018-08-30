#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    """prints titles of first 10 hot posts listed for a given subreddit"""
    r_subreddit = get('http://www.reddit.com/r/{}/hot.json'.
                      format(subreddit), headers={'User-Agent': 'Mybot'})
    try:
        subreddit_dict = r_subreddit.json()
        for i in range(10):
            print(subreddit_dict['data']['children'][i]['data']['title'])
    except:
        print(None)
