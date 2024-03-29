#!/usr/bin/python3
"""
Sends a POST request to the specified URL with the email provided as a parameter,
and then displays the decoded body of the response using UTF-8 encoding.
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))

