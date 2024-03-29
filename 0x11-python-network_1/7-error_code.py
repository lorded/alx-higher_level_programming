#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response."""

if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    response = get(url)
    error_message = 'Error code: {}'
    status_code = response.status_code
    print(error_message.format(status_code) if status_code >= 400 else response.text)

