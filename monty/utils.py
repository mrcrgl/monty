__author__ = 'mriegel'
import os
import inspect
import monty


def get_user_homedir():
    return os.getenv('USERPROFILE') or os.getenv('HOME')


def get_monty_dir():
    return os.path.join(os.path.dirname(inspect.getfile(monty)), os.pardir)
