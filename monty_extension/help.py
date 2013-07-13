from monty.extension.basic import BasicExtension
from monty.cli.stream import *


class MontyCliExtension(BasicExtension):
    """
    Extension: help
    """
    namespace = "help"
    aliases = ['-h', '--help']
    description = "Display this help"

    def route(self):
        StdOutput.write("Help message...")