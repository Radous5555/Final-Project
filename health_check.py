#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket

sender = "automation@example.com"
recipient = "student@example.com"
body = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_disk_usage():
    disk_usage = shutil.disk_usage("/")
    free_disk = disk_usage.free/disk_usage.total*100
    return free_disk > 20

def check_memory_usage():
    mem = psutil.virtual_memory()
    limit = 100 * 1024 * 1024  # 100MB
    return mem.available > limit

def check_localhost():
    return socket.gethostbyname("localhost") == "127.0.0.1"
    
if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

if not check_disk_usage():
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

if not check_memory_usage():
    subject = "Error - Available memory is less than 100MB"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)