#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get

# make request using the python requests lib
if __name__=="__main__":
    r = get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
