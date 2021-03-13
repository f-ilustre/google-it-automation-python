#!/usr/bin/env python3

import datetime
import run
import reports
import emails
import os

date_now = datetime.datetime.now().strftime("%c")


def process_fruit():

    pdf = ""

    for item in list2:
        name = item['name']
        weight = str(item['weight'])  # turn to string?
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"

    return pdf


if __name__ == "__main__":
    title = "Process Update on " + date_now
    list2 = run.process_desc()  # get the list of dictionaries
    pdf = process_fruit()  # turn it into the body of the pdf
    reports.generate_report("/tmp/processed.pdf", title, pdf)  # generate the report

    # initiate email variables
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ["USER"])
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = '/tmp/processed.pdf'  # os.getcwd() ?

    # generate email and send
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)

