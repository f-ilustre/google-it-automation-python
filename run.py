#!/usr/bin/env python3

import os
import requests

# uploads descriptions to Django server


def process_desc():

    directory = '/supplier-data/descriptions/'
    url = 'http://[localhost]/fruits/'
    list2 = []

    for file in os.listdir(directory):
        if not file.startswith('.'):
            with open(directory + file, 'r') as opened:
                info = opened.read().split("\n")
                filename = os.path.splitext(file)[0]
                feedback = {'name': info[0], 'weight': int(info[1].strip(' lbs')),
                            'description': info[2], 'image_name': filename + '.jpeg'}
                list2.append(feedback)
                response = requests.post(url, json=feedback)  # data or json?
                if response.status_code == 201:
                    print('Feedback successfully sent')
                else:
                    print(response.raise_for_status)

    return list2

process_desc()
