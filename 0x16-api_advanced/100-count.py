#!/usr/bin/python3
"""
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces)
"""
from collections import OrderedDict
from requests import get


def count_words(subreddit, word_list, after=None, match_dict={}):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces)
    Args:
        subreddit (str): subreddit
        word_list (list): list of words to count occurrences for
        after (str): refer to next page
        match_dict (dict): dictionary of frequency of words from word_list
        flag (int): indicate when match_dict is complete
    """
    try:
        r = get('https://www.reddit.com/r/{}/hot.json?limit=100&&'
                'after={}'.format(subreddit, after),
                headers={'User-Agent': 'bc'})
        sub_dict = r.json()

        if match_dict == {}:
            for w in word_list:
                match_dict[w] = 0

        after = sub_dict['data']['after']

        for i in range(len(sub_dict['data']['children'])):
            title_string = sub_dict['data']['children'][i]['data']['title']
            search_list = title_string.split()
            for word in search_list:
                for w in word_list:
                    if w.lower() == word.lower():
                        match_dict[w] += 1

        if after is None:
            descend_dict = OrderedDict(sorted(match_dict.items(),
                                              key=lambda x: x[1],
                                              reverse=True))
            zero_count = 0
            for k, v in descend_dict.items():
                if v != 0:
                    print("{}: {}".format(k, v))
                else:
                    zero_count += 1
            if zero_count == len(descend_dict):
                print()
        else:
            count_words(subreddit, word_list, after, match_dict)
    except:
        pass
