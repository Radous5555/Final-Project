#!/usr/bin/env python3

from PIL import Image
import os

directory = os.getcwd() + "/supplier-data/images/"

for image in os.listdir(directory):
    if image.endswith(".tif") or image.endswith(".tiff"):
        name, extension = os.path.splitext(image)
        old_img = Image.open(directory + image)
        old_img.resize((600,400)).convert("RGB").save(directory + name + ".jpeg", "jpeg")