__author__ = 'mriegel'
import requests
from monty.cli.stream import *
import json


class RestfulClient():

    peer = None
    auth = None

    last_response = None
    last_response_code = None

    def __init__(self, peer=None, auth=None):
        self.set_peer(peer)
        self.set_auth(auth)

    def put(self, url, params):
        StdOutput.activity("REQ", "PUT", self.get_url(url))

        credentials = self.get_credentials()
        r = requests.put(self.get_url(url), params=params, auth=credentials)
        self.last_response = r.json()
        self.last_response_code = r.status_code

        return self.process_response(r)

    def get(self, url):
        StdOutput.activity("REQ", "GET", self.get_url(url))

        credentials = self.get_credentials()
        r = requests.get(self.get_url(url), auth=credentials)
        self.last_response = r.json()
        self.last_response_code = r.status_code

        return self.process_response(r)

    def delete(self, url):
        StdOutput.activity("REQ", "DEL", self.get_url(url))

        credentials = self.get_credentials()
        r = requests.delete(self.get_url(url), auth=credentials)
        self.last_response = r.json()
        self.last_response_code = r.status_code

        return self.process_response(r)

    def process_response(self, r):
        success = False

        if r.status_code >= 200 and r.status_code < 300:
            success = True

        try:
            remote_code = self.last_response[u'code']
        except KeyError:
            remote_code = u'none'
            pass

        try:
            remote_message = self.last_response[u'message']
        except KeyError:
            remote_message = u''
            pass

        if success:
            StdOutput.write("RES - %d - [%s] %s" % (r.status_code, remote_code, remote_message))
        else:
            StdError.throw("RES - %d - [%s] %s" % (r.status_code, remote_code, remote_message))

        return success

    def get_status_code(self):
        if not self.last_response:
            return None

        return self.last_response.status_code

    def get_response(self):
        if not self.last_response:
            return {}

        return self.last_response

    def get_response_code(self):
        if not self.last_response_code:
            return None

        return self.last_response_code

    def get_credentials(self):
        if self.auth is None:
            return None

        user, password = self.auth.split(':')
        return user, password

    def set_peer(self, peer):
        self.peer = peer

    def set_auth(self, auth):
        self.auth = auth

    def get_url(self, path):
        return self.peer + path