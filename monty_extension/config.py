from monty.extension.basic import BasicExtension
from monty.cli.stream import *
from monty.config.loader import get_cfg
from pprint import pprint


class MontyCliExtension(BasicExtension):
    """
    Extension: user
    """
    namespace = "config"
    config = None

    def __init__(self):
        self.commands = {
            "show": self.show,
            "del": self.del_attr,
            "set": self.set_attr,
            "get": self.get_attr,
        }

    def route(self, args):

        try:
            config_name = args[0]
        except IndexError:
            return self.error("Missing arguments.")
            pass

        try:
            self.config = get_cfg(config_name)
        except NotImplementedError:
            return self.error("Config '"+config_name+"' cannot be found.")

        try:
            config_action = args[1]
        except IndexError:
            config_action = 'show'
            pass

        if config_action in self.commands:
            return self.commands[config_action](args[1:])

        return self.error("Action '"+config_action+"' cannot be found.")

    def show(self, args=[]):
        StdOutput.write("Config dump:")
        return pprint(self.config.read())

    def del_attr(self, args):
        config = self.config.read()

        try:
            key = args[1]
        except IndexError:
            return self.error("key wroing....")

        del config[key]
        self.config.write(config)

        StdOutput.write("Saved!")

        return self.show()

    def set_attr(self, args=[]):
        config = self.config.read()

        try:
            key, value = args[1:]
        except IndexError:
            return self.error("key value wroing....")

        config[key] = value
        self.config.write(config)

        StdOutput.write("Saved!")

        return self.show()

    def get_attr(self, args=[]):
        config = self.config.read()

        try:
            key = args[1]
        except IndexError:
            return self.error("key wroing....")

        if key in config:
            return StdOutput.write(config[key])

        return None
