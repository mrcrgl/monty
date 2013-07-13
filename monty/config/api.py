__author__ = 'mriegel'
from basic import BasicConfig
from monty.utils import get_monty_dir
import os


class ApiConfig(BasicConfig):
    path = os.path.join(get_monty_dir(), 'config/api.json')