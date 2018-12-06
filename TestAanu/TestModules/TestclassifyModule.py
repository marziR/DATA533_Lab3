
# coding: utf-8

# In[2]:


import unittest
from personal.fitness import classify


class TestBmicat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('Set Up')

    def test_bmicat(self):
        self.assertEqual(classify.bmicat(16), 'Underweight')
        self.assertEqual(classify.bmicat(23), 'Healthy')
        self.assertEqual(classify.bmicat(29), 'Overweight')
        self.assertEqual(classify.bmicat(33), 'Obese')
        self.assertEqual(classify.bmicat(52), 'Morbidly Obese')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
unittest.main(argv=[''], verbosity=2, exit=False)
