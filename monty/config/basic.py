__author__ = 'mriegel'
from monty.files.config import read as config_read
from monty.files.config import write as config_write


class BasicConfig():

    def get_file_path(self):
        return self.path

    def read(self):
        return config_read(self.get_file_path())

    def write(self, data):
        return config_write(self.get_file_path(), data)