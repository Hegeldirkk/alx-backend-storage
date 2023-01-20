#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker"""


import requests
from redis import Redis
r_count = Redis()
count = 0


def get_page(url: str) -> str:
    """exipring cache"""
    r_count.set(f"exp:{url}", count)
    response = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"exp:{url}", 10, r.get(f"exp:{url}"))
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
