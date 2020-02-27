import os
import re
from pathlib import Path

path = Path('Test')

def main(path, regex='', min_size=0):
    path = verify_path(path)
    regex = verify_regex(regex)
    min_size = verify_size(min_size)

    matching_paths = []
    for a,b,c in os.walk(path):
        ...

    return matching_paths


