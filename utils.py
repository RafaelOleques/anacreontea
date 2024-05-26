import os.path
from os import path
import os
from itertools import combinations

def create_directory(ref):
    if path.exists(ref) == False:
        os.mkdir(ref)

def create_directory_from_list(root, directory_list):
    path = root
    for directory in directory_list:
        path = f"{path}/{directory}"
        create_directory(path)

    return path