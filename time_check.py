import filescanner
import filescanner2
import timeit

from pathlib import Path

num = 25
print('Total items: ', len(filescanner2.main(r'D:\Anime To watch Pronto')))
print(timeit.timeit("""filescanner.main(r'D:\Anime To watch Pronto')""", 'import filescanner', number=num)/num, ' s')
print(timeit.timeit("""filescanner2.main(r'D:\Anime To watch Pronto')""", 'import filescanner2', number=num)/num, ' s')
