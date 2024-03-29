#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response."""

if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    query = argv[1] if len(argv) >= 2 else ""
    data = {'q': query}
    response = post(URL, data)

    content_type = response.headers.get('content-type')

    if content_type == 'application/json':
        result = response.json()
        if result:
            _id = result.get('id')
            name = result.get('name')
            if _id and name:
                print("[{}] {}".format(_id, name))
            else:
                print('No result')
        else:
            print('No result')
    else:
        print('Not a valid JSON')

