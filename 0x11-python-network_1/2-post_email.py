#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    # Initialize the POST data, starting with a dictionary
    post_dict = {"email": argv[2]}
    # Use the urlencode() function to encode the dictionary
    data_encode = urlencode(post_dict)
    # Encode the resulting string into bytes using UTF-8 encoding
    post_data = data_encode.encode("utf-8")
    # use the Request() to add the data to the url
    req = Request(argv[1], data=post_data)
    # make a POST request to the url
    with urlopen(req) as response:
        # read the response
        body = response.read()
        # print the decoded body in utf-8
        print(body.decode("utf-8"))
