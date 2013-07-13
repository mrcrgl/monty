from monty.cli.stream import *


class BasicExtension:
    """
    This is the basic extension for inheritance of extensions.
    """

    def route(self):
        StdError.throw("Missing route() method in extension!")