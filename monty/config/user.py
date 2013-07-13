__author__ = 'mriegel'
from basic import BasicConfig
from monty.utils import get_user_homedir
import os


class UserConfig(BasicConfig):
    path = os.path.join(get_user_homedir(), '.montyrc')