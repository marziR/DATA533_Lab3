
# coding: utf-8

# In[1]:


import unittest
from personal.fitness import measure


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('Set Up')

    def test_calc(self):
        self.assertEqual(measure.calc(81,1.80),25)
        self.assertEqual(measure.calc(60,1.80),18)
        self.assertEqual(measure.calc(76,1.50),33)
        self.assertEqual(measure.calc(102,1.50),45)
        self.assertEqual(measure.calc(65,1.70),22)

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
unittest.main(argv=[''], verbosity=2, exit=False)
