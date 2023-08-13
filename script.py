#!/usr/python3

import json


file = 'courses.json'
arr = [1,2,4]
try:
    with open("file",'+r') as f:
        filecontent = json.dump(arr, f)
        print(filecontent)
except FileNotFoundError:
    print('{} file not found'.format(file))








