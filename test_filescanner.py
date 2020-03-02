from pyfakefs.fake_filesystem_unittest import TestCase
import unittest
import filescanner


class TestFileScanner(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_verify_path(self):
        from pathlib import Path
        path = '/root/testfolder'
        self.fs.create_dir(path)
        self.assertEqual(filescanner.verify_path(path), Path(path))

    def test_verify_regex(self):
        import re
        self.assertEqual(filescanner.verify_regex(''), '')
        self.assertEqual(filescanner.verify_regex('.'), re.compile('.'))

    def test_verify_bytes(self):
        self.assertEqual(filescanner.verify_size(0), 0)
        self.assertEqual(filescanner.verify_size(-500), 0)
        self.assertEqual(filescanner.verify_size(10), 10)
        self.assertEqual(filescanner.verify_size(10.1), 10)
        self.assertEqual(filescanner.verify_size(10.9), 10)
        self.assertEqual(filescanner.verify_size(10.1), 10)

    def test_check_folder(self):
        from pathlib import Path
        import re
        path = Path('/Test/subfolder')
        self.fs.create_dir(path)
        self.assertEqual(filescanner.check_folder(path, '', 0), [])

        file = Path('/Test/subfolder/test.txt')
        self.fs.create_file(file, contents='test')
        self.assertEqual(filescanner.check_folder(path, '', 0), [file])
        self.assertEqual(filescanner.check_folder(path, '', 1), [file])
        self.assertEqual(filescanner.check_folder(path, '', 5), [])

        regex = re.compile(r'\.txt')
        self.assertEqual(filescanner.check_folder(path, regex, 0), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 3), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 4), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 5), [])

        regex = re.compile(r'\.csv')
        self.assertEqual(filescanner.check_folder(path, regex, 0), [])
        self.assertEqual(filescanner.check_folder(path, regex, 5), [])

    def test_check_file(self):
        from pathlib import Path
        import re

        path = Path('/Test/subfolder')
        file = Path('/Test/subfolder/test.txt')
        self.fs.create_file(file, contents='test')
        self.assertEqual(filescanner.check_folder(path, '', 0), [file])
        self.assertEqual(filescanner.check_folder(path, '', 1), [file])
        self.assertEqual(filescanner.check_folder(path, '', 5), [])

        regex = re.compile(r'\.txt')
        self.assertEqual(filescanner.check_folder(path, regex, 0), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 3), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 4), [file])
        self.assertEqual(filescanner.check_folder(path, regex, 5), [])

        regex = re.compile(r'\.csv')
        self.assertEqual(filescanner.check_folder(path, regex, 0), [])
        self.assertEqual(filescanner.check_folder(path, regex, 5), [])

if __name__ == '__main__':
    unittest.main()
