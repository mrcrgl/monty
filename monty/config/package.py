__author__ = 'mriegel'
from basic import BasicConfig
import os


class PackageConfig(BasicConfig):
    path = os.path.join(os.getcwd(), 'monty.json')