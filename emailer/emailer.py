#!/usr/bin/env python

import smtplib


class Emailer():

    def __init__(self, server=None):
        '''
            Init Emailer object

            Args:
                - server (smtplib.SMTP) - The SMTP Server to send emails
        '''

        if type(server) is smtplib.SMTP:
            self.server = server
        elif server is not None:
            raise TypeError("expected type smtplib.SMTP for server, received {0}".format(type(server)))

    def __del__(self):
        '''
            Safely close the SMTP server on __del__
        '''

        if self.server:
            self.server.quit()

    def configure_server(self, host, port, user=None, password=None):
        '''
            Configure the SMTP Server

            Args:
                - host (str) - The host address of the SMTP Server
                - port (str) - The port of the SMTP server
                - user (str) - If auth is required, the user to access the SMTP Server
                - password (str) - If auth is required, the password to access the SMTP Server
        '''

        smtpServer = smtplib.SMTP(host, port)
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.ehlo()

        if user is not None and password is not None:
            smtpServer.login(user, password)

        self.server = smtpServer

    def send_message(self, message):
        '''
            Send an email message

            Args:
                - message (emailer.Message) - Message to be sent
        '''

        self.server.sendmail(message.from_email, message.to_email, message.compose())
