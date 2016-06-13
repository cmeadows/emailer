#!/usr/bin/env python

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Message():

    def __init__(self, from_email=None, to_email=None, subject=None, plain_text=None, html=None, attachments=None):
        """
        Init a Message object

        Args:
            - plain_text (str) - The plain text content of the message
            - html (str) - The html of the message
            - to_email (str, list) - The recipients' email addresses
            - from_email (str) - The sender's email address
            - subject (str) - The subject of the email
            - attachments (list) - A list of attachments to be attached to the email
        """

        self.from_email = from_email or None
        self.to_email = to_email or None
        self.subject = subject or None
        self.plain_text = plain_text or None
        self.html = html or None
        self.attachments = attachments or []

        self._composed = None

    def compose(self, from_email=None, to_email=None, subject=None, plain_text=None, html=None, attachments=None):
        """
        Compose the Message as a single string

        Args:
            - plain_text (str) - The plain text content of the message
            - html (str) - The html of the message
            - to_email (str, list) - The recipients' email addresses
            - from_email (str) - The sender's email address
            - subject (str) - The subject of the email
            - attachments (list) - A list of attachments to be attached to the email
        """

        self.from_email = from_email or self.from_email
        self.to_email = to_email or self.to_email
        self.subject = subject or self.subject
        self.plain_text = plain_text or self.plain_text
        self.html = html or self.html
        self.attachments = attachments or self.attachments

        message = MIMEMultipart('alternative')

        if self.plain_text is not None:
            message.attach(MIMEText(self.plain_text, 'plain', 'utf-8'))

        if self.html is not None:
            message.attach(MIMEText(self.html, 'html', 'utf-8'))

        message.add_header('Content-Transfer-Encoding', 'base64')

        message['Subject'] = self.subject
        message['From'] = self.from_email

        if type(self.to_email) is list:
            message['To'] = ', '.join(self.to_email)
        else:
            message['To'] = self.to_email

        for attachment in attachments:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(attachment.get('file'))
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(attachment.get('filename')))
            message.attach(part)

        return message.as_string()
