__author__ = 'mriegel'
# See http://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-gzip-module-inside-of-python
import tarfile
import hashlib


class Compressor():

    @staticmethod
    def folder(file_path, folder):
        tar = tarfile.open(file_path, "w:bz2")
        tar.add(folder, arcname=".")
        tar.close()

        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()
