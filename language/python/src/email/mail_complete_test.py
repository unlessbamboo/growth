#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import base64
import socket
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


SUCCESS = "Send mail successful,OK!"
ERR_SMTP_SERVER_DISCONNECTED = "Mail server unexpectedly disconnects"
ERR_SMTP_SENDER_REFUSED = "Sender address refused"
ERR_SMTP_RECIPIENT_REFUSED = "All recipient address refused"
ERR_SMTP_DATA = "Mail server refused to accept the message data"
ERR_SMTP_CONNECT = "Connnect mail server occur error"
ERR_SMTP_HELO = "Mail server refused our HELO message"
ERR_SMTP_AUTHENTICATION = "Mail server authentication went wrong"
ERR_SMTP_UNKNOWN = "Unknown error"
ERR_DATA_FORMAT = "Sorry, data format is invalidate."


def _handle_attach(main, data):
    '''handle attachment'''
    # common attachment file
    if 'file' in data and not data['file']:
        fileAttach = data['file']
        for (_name, _data) in fileAttach:
            print('**********************')
            print('data: ', _data)
            att = MIMEText(base64.b64decode(_data), "plain", 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'filedir/attachment; "\
                "filename="{0}"'.format(_name)
            main.attach(att)

    # Embed picture
    if 'image' in data_dict and not data_dict['image']:
        imageAttach = data_dict['image']
        for (_name, _data) in imageAttach:
            att = MIMEImage(base64.b64decode(_data))
            att.add_header('Content-ID', '<{0}>'.format(_name))
            main.attach(att)


def create(data):
    '''Create a mail.

    : data_dict: a dictionary to save mail.
    '''
    error_msg = ''
    msg = ''
    try:
        main = MIMEMultipart('related')
        _handle_attach(main, data)
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print(str(main))
        main.attach(MIMEText(data['content'], 'html', 'utf-8'))

        main['Subject'] = data['subject']
        main['From'] = data['from']
        main['To'] = ','.join(data['recip'])
        msg = main.as_string()
    except KeyError:
        error_msg = ERR_DATA_FORMAT
    except Exception as msg:
        error_msg = '{}{}'.format(ERR_SMTP_UNKNOWN, msg)

    _rsp = {'result': False, 'error_msg': error_msg} if error_msg else None
    return msg, _rsp


def send(confDict, data):
    '''send plain mail.

    : data:          mail data.
    : confDict:      configure dictionary
    '''
    error_msg = ''
    try:
        if confDict['auth'] == 'ssl':
            server = smtplib.SMTP_SSL(confDict['server'], confDict['port'])
            server.ehlo()
            server.esmtp_features["auth"] = "LOGIN PLAIN"
        else:
            server = smtplib.SMTP(confDict['server'], confDict['port'])
            # server.set_debuglevel(1)
            server.esmtp_features['auth'] = 'LOGIN PLAIN'

        server.login(confDict['from'], confDict['passwd'])
        server.sendmail(confDict['from'], confDict['recip'], data)
        server.quit()
    except smtplib.SMTPServerDisconnected:
        error_msg = ERR_SMTP_SERVER_DISCONNECTED
    except smtplib.SMTPSenderRefused:
        error_msg = ERR_SMTP_SENDER_REFUSED
    except smtplib.SMTPRecipientsRefused:
        error_msg = ERR_SMTP_RECIPIENT_REFUSED
    except smtplib.SMTPDataError:
        error_msg = ERR_SMTP_DATA
    except smtplib.SMTPConnectError:
        error_msg = ERR_SMTP_CONNECT
    except smtplib.SMTPHeloError:
        error_msg = ERR_SMTP_HELO
    except smtplib.SMTPAuthenticationError:
        error_msg = ERR_SMTP_AUTHENTICATION
    except (socket.timeout, socket.error):
        error_msg = ERR_SMTP_CONNECT
    except KeyError:
        error_msg = ERR_DATA_FORMAT

    _rsp = {
        'result': False,
        'errmsg': error_msg} if error_msg else {
        'result': True}

    return _rsp


if __name__ == '__main__':
    png1 = '/tmp/1.png'
    if os.path.exists(png1):
        with open(png1, 'rb') as fp:
            image1Data = fp.read()
    else:
        image1Data = None
    png2 = '/tmp/2.png'
    if os.path.exists(png2):
        with open(png2, 'rb') as fp:
            image2Data = fp.read()
    else:
        image2Data = None

    file1 = '/tmp/attach1.png'
    if os.path.exists(file1):
        with open(file1, 'rb') as fp:
            attach1Data = fp.read()
    else:
        attach1Data = None
    file2 = '/tmp/attach2.txt'
    if os.path.exists(file2):
        with open(file2, 'r') as fp:
            attach2Data = fp.read()
    else:
        attach2Data = None

    data_dict = {}
    data_dict['image'] = []
    if not image1Data:
        data_dict['image'].append(image1Data)
    if not image2Data:
        data_dict['image'].append(image2Data)

    data_dict['file'] = []
    if not attach1Data:
        data_dict['file'].append(attach1Data)
    if not attach2Data:
        data_dict['file'].append(attach2Data)

    data_dict['subject'] = 'This is a test'
    data_dict['content'] = ('<b>This is a test</b>'
                            '<br><img src="cid: 1.png">'
                            '<br><img src="cid: 2.png">')
    data_dict['recip'] = ['unlessbamboo@163.com']
    data_dict['from'] = os.environ.get('MAIL_USERNAME')
    data_dict['auth'] = 'ssl'
    data_dict['passwd'] = os.environ.get('MAIL_PASSWD')
    data_dict['server'] = os.environ.get('MAIL_SERVER')
    data_dict['port'] = os.environ.get('MAIL_PORT')

    oss = True
    if oss:
        import requests
        import json
        rsp = requests.post(
            'http: //xiage.shitx.shit.com/v1/send/mail/',
            data=json.dumps(data_dict),
            headers={'Content-type': 'application/json'})
        print(rsp.text)
    else:
        print(data_dict['file'])
        _data, rsp = create(data_dict)
        if not rsp:
            rsp = send(data_dict, _data)
        print(rsp)
