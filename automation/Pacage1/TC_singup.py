import unittest


class SignupTest(unittest.TestCase):
    def test_by_email(self):
        print("signup by email")

    def test_by_fb(self):
        print("signup by FB")

    def test_by_twtter(self):
        print("signup by Twitter")


if __name__ == "__main__":
    unittest.main()