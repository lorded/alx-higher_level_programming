#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter and displays the body of the response.
"""

if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    response = post(url, data={'email': email})
    print(response.text)

