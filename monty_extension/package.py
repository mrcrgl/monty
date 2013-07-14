from monty.extension.basic import BasicExtension
from monty.client.montysheart import MontysHeartClient
from monty.config.loader import get_package_cfg
#from monty.cli.stream import *
# See http://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-gzip-module-inside-of-python
#import tarfile


class MontyCliExtension(BasicExtension):
    """
    Extension: package
    """
    namespace = "package"

    api = None

    def __init__(self):
        self.commands = {
            "commit": self.commit,
        }
        self.api = MontysHeartClient()

    def verify(self, args=[]):
        package_config = get_package_cfg()
        params = package_config.read()
        return self.api.package_verify(params=params)

    def commit(self, args=[]):
        verified = self.verify()

        print "Verified: ", verified