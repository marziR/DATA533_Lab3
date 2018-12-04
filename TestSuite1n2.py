import unittest 
from TestModule1 import TestCalc 
from TestModule2 import TestBmiCat



def my_suite(): 
    suite = unittest.TestSuite() 
    result = unittest.TestResult() 
    suite.addTest(unittest.makeSuite(TestCalc)) 
    suite.addTest(unittest.makeSuite(TestBmiCat)) 
    runner = unittest.TextTestRunner() 
    print(runner.run(suite)) 
my_suite()