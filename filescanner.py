import os
import re
from pathlib import Path

path = Path('Test')

def main(path, regex='', min_size=0):
    path = verify_path(path)
    regex = verify_regex(regex)
    min_size = verify_size(min_size)

    matching_paths = check_folder(path)
    return matching_paths

def verify_path(path):
    ...

    return path

def verify_regex(regex):
    ...

    return regex

def verify_size(min_size):
    ...

    return min_size

def check_file(filepath):
    valid = False
    ...
    return valid

def check_folder(path):
    matching_paths = []
    ...

    return matching_paths

