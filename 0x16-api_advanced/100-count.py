#!/usr/bin/python3
"""
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces)
"""
from requests import get
from collections import OrderedDict


def count_words(subreddit, word_list, after=None, match_dict={}, flag=0):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces)"""
    try:
        if after is None:
            r_before = get('http://www.reddit.com/r/{}/hot.json?limit=100'.
                           format(subreddit),
                           headers={'User-Agent': 'bc'})
            sub_dict = r_before.json()
        else:
            r_after = get('https://www.reddit.com/r/{}/hot.json?limit=100&&'
                          'after={}'.format(subreddit, after),
                          headers={'User-Agent': 'bc'})
            sub_dict = r_after.json()

        if after is None and match_dict != {}:
            descend_dict = OrderedDict(sorted(match_dict.items(),
                                       key=lambda x: x[1], reverse=True))
            for k, v in descend_dict.items():
                if v != 0:
                    print("{}: {}".format(k, v))
            flag = 1

        if after is None and match_dict == {}:
            for w in word_list:
                match_dict[w] = 0

        if flag == 0:
            for i in range(len(sub_dict['data']['children'])):
                title_string = sub_dict['data']['children'][i]['data']['title']
                search_list = title_string.split()
                for word in search_list:
                    for w in word_list:
                        if w.lower() == word.lower():
                            match_dict[w] += 1
            after = sub_dict['data']['after']
            count_words(subreddit, word_list, after, match_dict)

    except:
        print()

"""
if __name__ == '__main__':
    count_words('programming', ['python', 'java', 'javascript','scala'])
"""
