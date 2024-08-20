#!/usr/bin/env python3

import os
import datetime
from datetime import date
import reports

descriptions = os.getcwd() + "/supplier-data/descriptions/"

today = date.today()
date = today.strftime("%B %d, %Y")

paragraph = []
for file in os.listdir(descriptions):
    if file.endswith(".txt"):
        with open (descriptions + file) as read_file:
            lines = read_file.read().splitlines()
            new_lines = ["name: " + lines[0] + "<br/>" + "weight: " + lines[1]]
            paragraph.extend(new_lines)
paragraph_joined = "<br/><br/>".join(paragraph)

def main():
    reports.generate("/tmp/processed.pdf", "Processed Update on " + date, paragraph_joined)

if __name__ == "__main__":
    main()