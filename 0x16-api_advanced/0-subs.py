#!/usr/bin/python3
""" 0. How many subs? """

import requests


def number_of_subscribers(subreddit):
    """ Query reddit API & return no. of subs """
    if subreddit:
        resp = requests.get('http://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers={
                                'User-Agent': 'Python/requests:APIproject:
                                v1.0.0 (by /u/aaorrico23)'
                            }
               ).json()
        sub = resp.get("data", {}).get("subscribers", 0)
        return sub
    return 0
