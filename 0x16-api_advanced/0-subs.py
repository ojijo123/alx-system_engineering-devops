#!/usr/bin/python3

"""
 function that queries the Reddit API and returns the number of subscribers
 """
import request

def number_of_subscribers(subreddit):
    """Define the URL for the subreddit's about page in the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    """Set custom User-Agent to avoid Too Many Requests error"""
    headers = {'User-Agent': 'custom-agent/0.1'}

     if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
