#!/usr/bin/env python

import requests
import os

SHODAN_API_KEY = "bSzzRaCT7le7TGVwiZpIH3CoGRrqxr9w"  #os.environ['ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8']
ip = '173.254.22.76'

def ShodanInfo(ip):
    try:
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minify=True").json()
    except Exception as exception:
        result = {"error":"Information not available"}
    return result

print(ShodanInfo(ip))

# https://api.shodan.io/shodan/host/{ip}?key=ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8
