#!/usr/bin/python3
""" 1. Top Ten """

import requests as rq


def top_ten(subreddit):
    """ Print titles of top 10 hot posts """
    if subreddit:
        res = rq.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/aaorrico23)'},
                     params={'limit': 10}).json()
        pos_10 = res.get('data', {}).get('children', None)
        if pos_10:
            for post in pos_10:
                print(post.get('data', {}).get('title', None))
    print("None")
