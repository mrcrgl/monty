__author__ = 'mriegel'
import json


def read(file_path):
    try:
        json_data = open(file_path)

        data = json.load(json_data)
        json_data.close()
        return data
    except IOError:
        return {}


def write(file_path, data):
    json_string = json.dumps(data)
    fo = open(file_path, "wb")
    fo.write(json_string)
    return True