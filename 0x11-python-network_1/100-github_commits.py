#!/usr/bin/python3
"""
script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = 'https://developer.github.com/v3/repos/{}/{}/commits/'.format(user, repo)
    r = get(url)
    commit_list = r.json()
    for commit in commit_list[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
