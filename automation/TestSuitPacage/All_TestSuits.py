import unittest

from Pacage1.TC_login import LoginTest
from Pacage1.TC_singup import SignupTest

from Pacage2.TC_Payment import Payment
from Pacage2.TC_Return import PaymentReturn



# getting TESTS from all the TEST CASES (Login ,Signup, Payment, Return)

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Payment)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)



# creating TEST SUIT

sanityTestSuit = unittest.TestSuite([tc1, tc2])
funtionalTestSuit = unittest.TestSuite([tc3, tc4])
masterTestSuit = unittest.TestSuite([tc1, tc2, tc3, tc4])



# RUNNING test suits

#unittest.TextTestRunner().run(sanityTestSuit)
#unittest.TextTestRunner().run(funtionalTestSuit)
unittest.TextTestRunner(verbosity=2).run(masterTestSuit)