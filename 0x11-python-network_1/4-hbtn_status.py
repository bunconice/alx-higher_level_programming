#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get

r = get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r.text))
