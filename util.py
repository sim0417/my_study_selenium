import os


def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
