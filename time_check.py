import filescanner2
import timeit

test_dir = r'/home/example'
num = 25
print('Total items: ', len(filescanner2.main(test_dir)))
print(timeit.timeit(f"""filescanner.main(r'{test_dir}')""", 'import filescanner', number=num)/num, ' s')
print(timeit.timeit(f"""filescanner2.main(r'{test_dir}')""", 'import filescanner2', number=num)/num, ' s')
