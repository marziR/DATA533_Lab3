import unittest
from personal.fitness.measure import calc
    
class TestCalc(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        print('setupClass')
    
    def setUp(self):
        print('Set Up')

    def test_calc(self):
        self.assertEqual(calc(60,1.6),23)
        self.assertEqual(calc(85,1.8),26)
        self.assertEqual(calc(65,1.72),21)
        self.assertEqual(calc(85,1.53),36)
        self.assertEqual(calc(60,1.76),19)
        self.assertEqual(calc(85,1.88),24)
    
    @classmethod 
    def tearDownClass(cls): 
        print('teardownClass')
        
    def tearDown(self):
        print('Tear Down')
        
unittest.main(argv=[''], verbosity=2, exit=False) 