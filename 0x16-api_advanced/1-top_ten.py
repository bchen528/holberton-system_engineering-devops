#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid subreddit is given,
return 0
"""
from requests import get
from sys import argv


def top_ten(subreddit):
    """returns number of subscribers for a given subreddit"""
    r_subreddit = get('http://www.reddit.com/r/{}/hot.json'.
                      format(subreddit), headers={'User-Agent': 'Mybot'})
    try:
        subreddit_dict = r_subreddit.json()
        for i in range(10):
            print(subreddit_dict['data']['children'][i]['data']['title'])
    except:
        print(None)
