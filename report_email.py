#!/usr/bin/env python3

import os
import datetime
from datetime import date
import reports
import emails

descriptions = os.getcwd() + "/supplier-data/descriptions/"
pdf_path = "/tmp/processed.pdf"
""" Insert mail server address here """
mail_url = "IP.ADDY.GOES.HERE/webmail"
today = date.today()
date = today.strftime("%B %d, %Y")

paragraph = []
for file in os.listdir(descriptions):
    if file.endswith(".txt"):
        with open (descriptions + file) as read_file:
            lines = read_file.read().splitlines()
            pdf_lines = ["name: " + lines[0] + "<br/>" + "weight: " + lines[1]]
            paragraph.extend(pdf_lines)
paragraph_joined = "<br/><br/>".join(paragraph)

def main():
    reports.generate(pdf_path, "Processed Update on " + date, paragraph_joined)
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, pdf_path)
    emails.send_email(message, mail_url)

if __name__ == "__main__":
    main()