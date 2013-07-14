__author__ = 'riegel'
import getpass


class StdInput:
    """
    Foo
    """
    @staticmethod
    def read(prompt):
        return raw_input(prompt)

    @staticmethod
    def read_password(prompt='Password: '):
        return getpass.getpass(prompt)


class StdOutput:
    """
    Foo
    """
    @staticmethod
    def write(message):
        print(message)

    @staticmethod
    def activity(type, code, message, status=None):
        if status:
            print ("%s - %d - [%s] %s" % (type, status, code, message))
        else:
            print ("%s - [%s] %s" % (type, code, message))


class StdError:
    """
    asf
    """
    @staticmethod
    def throw(message):
        print (message)
        return ""