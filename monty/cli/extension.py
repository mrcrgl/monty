__author__ = 'riegel'
import sys
import os
import re
import imp

def finder():
    extensions = {}

    for path in sys.path:
        extension_path = os.path.join(path, 'monty_extension')
        packages = []
        packages += check_path_for_extensions(extension_path)

        for package in packages:
            instance, namespace = load_from_file(os.path.join(extension_path, package))
            extensions[namespace] = instance
            #extensions[package] = imp.load_source(package, extension_path)

    return extensions


def load_from_file(filepath):
    class_inst = None
    expected_class = 'MontyCliExtension'

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = py_mod.MontyCliExtension()

    return class_inst, mod_name


def check_path_for_extensions(extension_path):

    if (os.path.isdir(extension_path) == False):
        return []

    isfile = re.compile(r'[a-z]+\.py$')
    packages = []
    for file in os.listdir(extension_path):
        if (isfile.match(file)):
            packages.append(file)

        #packages.append(os.path.join(extension_path, file))

    return packages