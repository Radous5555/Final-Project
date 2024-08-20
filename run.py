#! /usr/bin/env python3

import os
import requests
import re
import json

descriptions = os.getcwd() + "/supplier-data/descriptions/"

""" paste the url here """
url = "IP.ADDY.GOES.HERE/fruits"

data = []

for file in os.listdir(descriptions):
    if file.endswith(".txt"):
        name, extension = os.path.splitext(file)
        with open(descriptions + file) as read_file:
            lines = read_file.read().splitlines()
            weight = re.findall(r"\d+", lines[1])
            dictionary = {"name": lines[0], "weight": int(weight[0]), "description": lines[2],"image_name": name + ".jpeg"}
            data.append(dictionary)

data_json = json.dumps(data)
data_sent = requests.post(url, json=data_json)
print(data_sent.status_code)