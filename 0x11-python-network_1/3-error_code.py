#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))
