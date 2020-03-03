import os
import re
import pathlib

path = '.'  # pathlib.Path(r'D:\Anime To watch Pronto')
regex = '.mp4'
bytes = 200 * 1000 * 1000


def main(path, regex='', size_bytes=0):
    path = verify_path(path)
    regex = verify_regex(regex)
    size_bytes = verify_size(size_bytes)

    matching_paths = check_folder(path, regex, size_bytes)

    return matching_paths


def verify_path(path):
    if isinstance(path, str):
        path = pathlib.Path(path)
        exist = path.exists()
    elif not isinstance(path, pathlib.PurePath):
        exist = False
    else:
        exist = path.exists()

    while not exist:
        print('Folder path not valid, please enter a valid path')
        path = input('Path: ')
        path = pathlib.Path(path)

        exist = path.exists()
    return path


def verify_regex(regex):
    try:
        re.compile(regex)
        is_valid = True
    except re.error:
        is_valid = False
    except TypeError:
        is_valid = False

    if (not is_valid) or (regex == ''):
        regex = ''
    else:
        regex = re.compile(regex)

    return regex


def verify_size(size_bytes):
    try:
        size_bytes = int(size_bytes)
    except ValueError:
        raise ValueError('Invalid entry for size restriction, enter a valid integer')

    if size_bytes < 0:
        size_bytes = 0

    return size_bytes


def check_folder(path, regex, size_bytes):
    from pathlib import Path
    matching_paths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            filepath = Path(root).joinpath(name)
            if check_file(filepath, regex, size_bytes):
                matching_paths.append(filepath)
    return matching_paths


def check_file(filepath, regex, size_bytes):
    check_bytes = size_bytes > 0
    check_regex = regex != ''

    if check_bytes and not check_regex:  # bytes check
        valid = filepath.lstat().st_size > size_bytes
    elif not check_bytes and check_regex:  # regex check
        valid = regex.search(filepath.name) is not None
    elif check_bytes and check_regex:  # bytes and regex check
        valid = (filepath.lstat().st_size >= size_bytes) and (regex.search(filepath.name) is not None)
    else:  # pass all
        valid = True

    return valid


if __name__ == '__main__':
    paths = main(path, regex, bytes)

    for p in paths: print(p)
