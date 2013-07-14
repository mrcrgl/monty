from monty.cli.stream import *


class BasicExtension:
    """
    This is the basic extension for inheritance of extensions.
    """
    commands = {}

    def route(self, args):

        try:
            config_action = args[0]
        except IndexError:
            config_action = 'show'
            pass

        if config_action in self.commands:
            return self.commands[config_action](args[1:])

        return self.error("Action '"+config_action+"' cannot be found.")

    def error(self, message=None):
        if message:
            StdOutput.write(message)

        self.help()

    def help(self):
        StdOutput.write("Help not defined!")