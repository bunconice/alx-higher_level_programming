#!/usr/bin/python3
"""
given username and pw as param, get your id from Github api
usage: ./10-my_github.py [github_username] [github_pw]
"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    password = argv[2]
    basic = HTTPBasicAuth(user, password)
    r = get(url, auth=basic)
    print(r.json().get('id'))
