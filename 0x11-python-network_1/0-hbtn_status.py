#!/usr/bin/python3
"""Reads the contents of https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)


    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))

