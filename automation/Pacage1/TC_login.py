import unittest

class LoginTest(unittest.TestCase):
    def test_by_email(self):
        print("login by email")

    def test_by_fb(self):
        print("login by FB")

    def test_by_twtter(self):
        print("login by Twitter")

if __name__=="__main__":
    unittest.main()

