#!/usr/bin/python3
"""
Sends a request to URL Displays the value of the
X-Request-Id variable
found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        x_request_id = None
        for header in headers:
            if header[0] == "X-Request-Id":
                x_request_id = header[1]
                break
        
        if x_request_id is not None:
            print(x_request_id)
            
