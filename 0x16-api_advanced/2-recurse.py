#!/usr/bin/python3
""" Recursive """

import requests as rq


def recurse(subreddit, hot_list=[], after=None):
    """ Return titles of all hot articles """
    if subreddit:
        res = rq.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/aaorrico23)'},
                     params={'after': after}).json()
        pos_10 = res.get('data', {}).get('children', None)
        after = res.get('data', {}).get('after', None)
        if pos_10 is None or (len(pos_10) > 0 and pos_10[0].get('kind') != 't3'):
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            for post in pos_10:
                hot_list.append(post.get('data', {}).get('title', None))
        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
