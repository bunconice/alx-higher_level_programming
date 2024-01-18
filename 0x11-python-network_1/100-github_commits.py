#!/usr/bin/python3
"""
given repo and owner name as argvs, use Github API to list last 10 commits
usage: ./100-github_commits.py [github_repo] [github_owner]
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    # get user and repo name from the command line
    user = argv[2]
    repo = argv[1]
    # format the user and repo name into the url
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        user, repo)
    # make request using the python requests lib
    response = get(url)
    # decode the response using json decoder
    list_commits = response.json()
    # iterate through to get the first 10 key value-pair
    for commit in list_commits[0:10]:
        print(commit['sha'], end=': ')
        print(commit['commit']['author']['name'])
