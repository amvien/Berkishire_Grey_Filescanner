
    Write a python script to recurse a given directory location and return a list of files whose names match a regex
    (or maybe just whose size is > than some number)
        - filescanner2.py
        - regex and size limits
    Write unit tests for the above.  Demonstrate your code coverage and justify it (i.e. why is this good enough)
        - python -m unittest test_filescanner2.py
        - 97% coverage - exception to the code for running at top-level
            coverage run -m unittest test_filescanner2.py
            coverage report -m
    Demonstrate execution time.  How might this be improved
        - os.walk 6x faster than listdir solution
        - spliting operations over threads using listdir.

    
    Tested in - Python 3.8