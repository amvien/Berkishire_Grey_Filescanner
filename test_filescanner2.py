from pyfakefs.fake_filesystem_unittest import TestCase
import unittest
from unittest import mock
import filescanner2 as filescanner


class TestFileScanner(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_main(self):
        from pathlib import Path

        path = Path('/Test/subfolder')
        file = path.joinpath('test.txt')
        self.fs.create_file(file, contents='test')
        self.assertEqual(filescanner.main(path, '', 0), [file])

    @mock.patch('filescanner2.input', create=True)
    def test_verify_path(self, mocked_input):
        from pathlib import Path
        path = '/root/testfolder'
        self.fs.create_dir(path)
        self.assertEqual(filescanner.verify_path(path), Path(path))
        self.assertEqual(filescanner.verify_path(Path(path)), Path(path))

        mocked_input.side_effect = [path]
        self.assertEqual(filescanner.verify_path(r'/wrong/folder'), Path(path))

        mocked_input.side_effect = [path]
        self.assertEqual(filescanner.verify_path(3241), Path(path))

    def test_verify_regex(self):
        import re
        self.assertEqual(filescanner.verify_regex(''), '')
        self.assertEqual(filescanner.verify_regex('.'), re.compile('.'))
        self.assertEqual(filescanner.verify_regex('(3'), '')
        self.assertEqual(filescanner.verify_regex(3), '')

    def test_verify_bytes(self):
        self.assertEqual(filescanner.verify_size(0), 0)
        self.assertEqual(filescanner.verify_size(-500), 0)
        self.assertEqual(filescanner.verify_size(10), 10)
        self.assertEqual(filescanner.verify_size(10.1), 10)
        self.assertEqual(filescanner.verify_size(10.9), 10)
        self.assertEqual(filescanner.verify_size(10.1), 10)
        with self.assertRaises(ValueError):
            filescanner.verify_size('cat')

    def test_check_folder(self):
        from pathlib import Path
        import re
        top_path = Path('/Test/')
        path = top_path.joinpath('subfolder')
        self.fs.create_dir(path)
        self.assertEqual(filescanner.check_folder(path, '', 0), [])
        self.assertEqual(filescanner.check_folder(top_path, '', 0), [])

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

        file = Path('/Test/subfolder/test.txt')
        self.fs.create_file(file, contents='test')
        self.assertEqual(filescanner.check_file(file, '', 0), True)
        self.assertEqual(filescanner.check_file(file, '', 1), True)
        self.assertEqual(filescanner.check_file(file, '', 5), False)

        regex = re.compile(r'\.txt')
        self.assertEqual(filescanner.check_file(file, regex, 0), True)
        self.assertEqual(filescanner.check_file(file, regex, 3), True)
        self.assertEqual(filescanner.check_file(file, regex, 4), True)
        self.assertEqual(filescanner.check_file(file, regex, 5), False)

        regex = re.compile(r'\.csv')
        self.assertEqual(filescanner.check_file(file, regex, 0), False)
        self.assertEqual(filescanner.check_file(file, regex, 5), False)


if __name__ == '__main__':
    unittest.main()
