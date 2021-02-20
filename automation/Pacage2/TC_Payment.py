import unittest


class Payment(unittest.TestCase):
    def test_by_rupee(self):
        print("payment by rupee")

    def test_by_doller(self):
        print("payment by doller")


if __name__ == "__main__":
    unittest.main()