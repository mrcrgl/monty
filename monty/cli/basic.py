from monty.cli.extension import finder as extension_finder
import sys


class MontyCli:

    extensions = extension_finder()
    argument_map = {}
    fallback_extension = 'help'

    def __init__(self):
        for extension in self.extensions:
            self.register_extension(extension)

        self.route()

    def register_extension(self, extension):

        if not hasattr(extension, 'namespace'):
            return None

        self.register_argument(extension.namespace, extension.namespace)

        if hasattr(extension, 'aliases'):
            for alias in extension.aliases:
                self.register_argument(extension.namespace, alias)

    def register_argument(self, argument, namespace):
        print "Namespace registered", namespace
        self.argument_map[argument] = namespace

    def route(self):
        try:
            arg = sys.argv[1] or None
        except IndexError:
            arg = None

        if arg and arg in self.extensions:
            return self.extensions[arg].route(sys.argv[2:])

        self.extensions[self.fallback_extension].route(sys.argv[2:])