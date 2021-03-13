#!/usr/bin/env python3

import psutil
import shutil
import os
import emails
import socket

def cpu_check():  # checks if the cpu usage is over 80%
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage > 80


def disc_space_check():  # Check if the available disk space is lower than 20%
    total, used, free = shutil.disk_usage('/')
    percentage = (free / total) * 100
    return percentage < 20


def available_memory_check():  # Check if available memory is less than 500mb
    total, available, *other = psutil.virtual_memory()
    available_mb = available / 1024 ** 2
    return available_mb < 500


def hostname_check():  # Report an error if the hostname "localhost" cannot be resolved to 127.0.0.1
    local_ip = socket.gethostbyname('localhost')
    return local_ip != "127.0.0.1"


def email_warning(error):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

if cpu_check():
    error = "Error - CPU usage is over 80%"
    email_warning(error)

if disc_space_check():
    error = "Error - Available disk space is less than 20%"
    email_warning(error)

if available_memory_check():
    error = "Error - Available memory is less than 500MB"
    email_warning(error)

if hostname_check():
    error = "Error - localhost cannot be resolved to 127.0.0.1"
    email_warning(error)

