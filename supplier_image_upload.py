#!/usr/bin/env python3

import requests
import os

# uploads converted images to the web server

url = "http://localhost/upload/"
path = "supplier-data/images/"

for image in os.listdir(path):
    if image.endswith(".jpeg"):
        with open(path + image, 'rb') as opened:
            r = requests.post(url, files = {'file': opened})

