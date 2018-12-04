
# coding: utf-8

# In[2]:


import unittest
from personal.fitness import classify

@classmethod 
def setUpClass(cls): 
    print('setupClass')

class TestBmicla(unittest.TestCase):
    def setUp(self):
        print('Set Up')
    
    def test_bmicla(self):
        self.assertEqual(bmicla(16), 'Underweight')
        self.assertEqual(bmicla(23), 'Healthy')
        self.assertEqual(bmicla(29), 'Overweight')
        self.assertEqual(bmicla(33), 'Obese')
        self.assertEqual(bmicla(52), 'Morbidly Obese')
        
    def tearDown(self):
        print('Tear Down')  
        
@classmethod 
def tearDownClass(cls): 
    print('teardownClass') 

