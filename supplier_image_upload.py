#!/usr/bin/env python3

import requests
import os

directory = os.getcwd() + "/supplier-data/images/"

""" paste the url here """
url = "IP.ADDY.GOES.HERE/upload/"

for new_image in os.listdir(directory):
    """ this will send all jpegs, regardless of whether or not they've already been uploaded """
    if new_image.endswith(".jpeg"):
        with open(directory + new_image, "rb") as opened:
            sent = requests.post(url, files={"file": opened})
            print(sent.status_code)