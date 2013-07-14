from monty.extension.basic import BasicExtension
from monty.client.montysheart import MontysHeartClient
from monty.config.loader import get_user_cfg
from monty.cli.stream import *


class MontyCliExtension(BasicExtension):
    """
    Extension: user
    """
    namespace = "user"
    #config = None

    api = None

    def __init__(self):
        self.commands = {
            "login": self.login,
            "register": self.register,
        }
        self.api = MontysHeartClient()

    def login(self, args=[]):
        try:
            username = StdInput.read("Username: ")
            password = StdInput.read_password()
        except KeyboardInterrupt:
            StdOutput.write("Interrupted")
            return
            pass

        self.api.set_auth(':'.join((username, password)))
        success = self.api.login()
        #print "Success: ", success
        if success:
            self.save_local_credentials(username, password)

        #print self.api.get_response()

        return None

    def register(self, args=[]):
        try:
            email = StdInput.read("Email: ")
            username = StdInput.read("Username: ")
            password = StdInput.read_password()
        except KeyboardInterrupt:
            StdOutput.write("Interrupted")
            return
            pass

        params = {
            "email": email,
            "username": username,
            "password": password,
        }

        success = self.api.register(params)
        #print "Success: ", success
        if success:
            self.save_local_credentials(username, password)

        #print self.api.get_response()

        return None

    def save_local_credentials(self, username, password):
        user_config = get_user_cfg()
        settings = user_config.read()
        key = u'authentication'
        settings[key] = ':'.join((username, password))
        user_config.write(settings)