import time
import unittest


class CryptographyTest(unittest.TestCase):
    def test_import(self):
        start = time.time()
        from cryptography import x509

        end = time.time()
        print("Imported cryptography.x509 in %0.2fs" % (end - start))
