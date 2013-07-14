from monty.extension.basic import BasicExtension
from monty.client.montysheart import MontysHeartClient
from monty.config.loader import get_package_cfg
#from monty.cli.stream import *
import tempfile
import os
from monty.files.compress import Compressor


class MontyCliExtension(BasicExtension):
    """
    Extension: package
    """
    namespace = "package"

    converted = {
        "name": u'name',
        "version": u'version',
    }

    api = None

    def __init__(self):
        self.commands = {
            "commit": self.commit,
        }
        self.api = MontysHeartClient()

    def verify(self, params):

        return self.api.package_verify(params=params)

    def commit(self, args=[]):
        package_config = get_package_cfg()
        params = package_config.read()

        verified = self.verify(params=params)

        if not verified:
            return

        print params

        package_name = params[u'name']
        package_version = params[u'version']
        filename = "/{0}-{1}.tbz2".format(package_name, package_version)

        print filename

        temp_folder = tempfile.gettempdir()
        file_path = "".join(os.path.join((temp_folder, filename)))

        print type(file_path)

        if os.path.isfile(file_path):
            os.remove(file_path)

        md5_checksum = Compressor.folder(file_path, os.getcwd())

        print "File: ", file_path
        print "Checksum: ", md5_checksum

        success = self.api.package_commit(params=params, file=file_path, filename=filename, checksum=md5_checksum)

        print "Success: ", success

        #os.remove(file_path)