import unittest
import filescanner


class TestFileScanner(unittest.TestCase):

    def test_verify_path(self):
        from pathlib import Path
        path = '.'
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


if __name__ == '__main__':
    unittest.main()
