# coding:utf8
"""
Send an multipart email with HTML and plain text alternatives. The message
should be constructed as a plain-text file of the following format:

    From: Your Name <your@email.com>
    To: Recipient One <recipient@to.com>
    Subject: Your subject line
    ---
    Markdown content here
The script accepts content from stdin and, by default, prints the raw
generated email content to stdout.
Preview your message on OS X by invoking the script with `-p` or
`--preview`, and it will open in your default mail client.
To send the message, invoke with `-s` or `--send`. You must have a
JSON file in your home directory named `.markdown-to-email.json`
with the following keys:
    {
        "username": "smtp-username",
        "smtp": "smtp.gmail.com:587",
        "password": "your-password"
    }
Enjoy!
"""


import os
import sys
import json
import argparse
import smtplib
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imp

try:
    import pygments
    import markdown
except ImportError:
    print('This script requires pygements and markdown to be installed.')
    print('Please:')
    print('   pip install pygments markdown')
    sys.exit(0)
else:
    imp.reload(sys)
    sys.setdefaultencoding('utf8')


# define arguments
parser = argparse.ArgumentParser(
    description='Format and send markdown-based emails.',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=__doc__)
parser.add_argument('-p', '--preview', action='store_true',
                    help='Preview the email in Apple Mail.')
parser.add_argument('-s', '--send', action='store_true',
                    help='Send the email using your configuration.')
parser.add_argument('-f', '--file',
                    help='Read the email content from special markdown file.')
args = parser.parse_args()

# read in raw message content
if args.file:
    raw_content = open(args.file, mode='r').read()
else:
    raw_content = sys.stdin.read()

# split out the headers from the markdown message body
header_content, markdown_content = raw_content.split('--', 1)

# render the markdown into HTML
css = subprocess.check_output(['pygmentize', '-S', 'default', '-f', 'html'])
markdown_content = markdown_content.strip()
html_content = markdown.markdown(markdown_content, ['extra', 'codehilite'])
html_content = '<style type="text/css">' + css + '</style>' + html_content

# create a multipart email message
message = MIMEMultipart('alternative')

# parse the headers
headers = {}
for line in header_content.strip().split('\n'):
    if not line.strip():
        continue
    key, value = line.split(':', 1)
    headers[key.strip()] = value.strip()

# set the headers
message['To'] = headers.get('To', '')
message['From'] = headers.get('From', '')
message['Subject'] = headers.get('Subject', 'No subject')

# attach the message parts
message.attach(MIMEText(markdown_content, 'plain', 'utf8'))
message.attach(MIMEText(html_content, 'html', 'utf8'))

if args.send:
    to = [t.strip(' ') for t in message['To'].split(', ')]

    with open(os.path.expanduser('~/.data/.markdown-to-email.json'), 'rb') as f:
        config = json.loads(f.read())
        server = smtplib.SMTP(config['smtp'])
        server.starttls()
        server.login(config['username'], config['password'])
        print('From:', message['From'])
        print('To:', to)
        server.sendmail(message['From'], to, message.as_string())
        server.quit()
elif args.preview:
    open('/tmp/preview.eml', 'w').write(message.as_string())
    os.system('open -a Mail /tmp/preview.eml')
else:
    print(message.as_string())
