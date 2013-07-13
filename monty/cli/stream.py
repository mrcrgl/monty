__author__ = 'riegel'


class StdInput:
    """
    Foo
    """
    @staticmethod
    def read():
        return ""

class StdOutput:
    """
    Foo
    """
    @staticmethod
    def write(message):
        print(message)

class StdError:
    """
    asf
    """
    @staticmethod
    def throw(message):
        print (message)
        return ""