import os
import re
import pathlib

path = pathlib.Path('/home/xaegrek/PycharmProjects/Berkishire_Grey_Filescanner')
regex = ''
bytes = 0

def main(path, regex='', size_bytes=0):
    path = verify_path(path)
    regex = verify_regex(regex)
    size_bytes = verify_size(size_bytes)

    matching_paths = check_folder(path, regex, size_bytes)
    return matching_paths

def verify_path(path):
    if  isinstance(path, str):
        path = pathlib.Path(path)

    if not (isinstance(path, pathlib.PurePath) or path.exists()):
        while True:
            print('Folder path not valid, please enter a valid path')
            path = input('Path: ')
            path = pathlib.Path(path)

            if path.exists():
                break
    return path

def verify_regex(regex):
    try:
        re.compile(regex)
        is_valid = True
    except re.error:
        is_valid = False

    if (not is_valid) or (regex == ''):
        regex = ''
    else:
        regex = re.compile(regex)

    return regex

def verify_size(size_bytes):
    size_bytes = int(size_bytes)

    if size_bytes < 0:
        size_bytes = 0

    return size_bytes

def check_folder(path, regex, size_bytes):
    matching_paths = []
    possible_paths = [path.joinpath(s) for s in os.listdir(path)]

    for sub in possible_paths:
        if sub.is_file():
            if check_file(sub, regex, size_bytes):
                matching_paths.append(sub)

        elif sub.is_dir():
            matching_paths = matching_paths + check_folder(sub, regex, size_bytes)

    return matching_paths

def check_file(filepath, regex, size_bytes):
    valid_bytes = False
    valid_regex = False

    if size_bytes > 0:
        valid_bytes = filepath.lstat().st_size > size_bytes

    if regex != '':
        valid_regex = regex.search(filepath.name) != None

    if (size_bytes <=0) and (regex == ''):
        valid = True
    else:
        valid = valid_bytes and valid_regex

    return valid


if __name__ == '__main__':
    paths = main(path,regex, bytes)

    for p in paths: print(p)