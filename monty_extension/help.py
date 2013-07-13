from monty.extension.basic import BasicExtension
from monty.cli.stream import *
from monty.config.loader import get_user_cfg, get_api_cfg


class MontyCliExtension(BasicExtension):
    """
    Extension: help
    """
    namespace = "help"
    aliases = ['-h', '--help']
    description = "Display this help"

    def route(self, args):
        StdOutput.write("Help message...")
        cfg = get_api_cfg()
        print cfg.path