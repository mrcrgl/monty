__author__ = 'mriegel'
from monty.config.loader import get_api_cfg, get_user_cfg
from restful import RestfulClient


class MontysHeartClient(RestfulClient):

    config = None

    def __init__(self):
        self.config = get_api_cfg().read()
        self.set_peer(self.config[u'montysheart_peer'])
        try:
            self.set_auth(get_user_cfg().read()[u'authentication'])
        except:
            pass

    def register(self, params):
        path = '/user'
        success = self.put(path, params=params)
        #print "Test: ", self.last_response
        return success

    def login(self):
        path = '/user/auth'
        success = self.get(path)
        #print self.get_response()
        return success

    def get_user(self, email):
        path = '/user/'+email

    def package_verify(self, params):
        path = '/py/package/verify'
        success = self.put(path, params=params)
        return success

    def package_commit(self, params):
        path = '/py/package/commit'
        success = self.put(path, params=params)
        return success