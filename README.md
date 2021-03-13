# google-it-automation-python

Final project files for the Google IT Automation with Python Professional Certificate in Coursera.

### 1. changeImage.py
Used the PIL Library to update .TIFF files in a folder to new specifications:
a) 600 x 400 pixel
b) .JPEG format

### 2. supplier_image_upload.py
Uploads the converted images to the web server using a POST request.

### 3. run.py
Reads from .txt files in a folder, uploads the text to the web server, and stores
the text uploaded in a variable for an email script.

### 4. reports.py
Generates a PDF file using Reportlab's Platypus. 

### 5. emails.py
Generates an email using email.message module and sends the email using the smtplib module

### 6. report_email.py
Reads some data from variable stored from run.py, turns it into a string as an argument for reports.generate_report().
This script also sets the variables and calls for emails.generate_email() and emails.send_email(). 

### 7. health_check.py
The script will run in the background (see cron_file) to check the following:
a) CPU usage is over 80%
b) Available disk space is lower than 20%
c) Available memory is less than 500mb
d) The hostname cannot be resolved to "127.0.0.1"

An email will be sent if the metrics is beyond the threshold using the emails.generate_email() method.
