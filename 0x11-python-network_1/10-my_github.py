#!/usr/bin/python3
"""
Uses GitHub API to display the user ID associated with provided GitHub credentials (username and password).
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    user_data = response.json()

    user_id = user_data.get('id')
    print(user_id)

