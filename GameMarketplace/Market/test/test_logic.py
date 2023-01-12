from django.test import TestCase
from .some1 import summ
from django import setup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
setup()



class LogicTestCase(TestCase):
    def test_plus(self):
        result = summ(1, 2, "+")
        self.assertEqual(3, result)
        
    def test_minus(self):
        result = summ(1, 2, "-")
        self.assertEqual(-1, result)
    
    def test_multiplie(self):
        result = summ(1, 2, "*")
        self.assertEqual(2, result)
        
    def test_delite(self):
        result = summ(1, 2, "/")
        self.assertEqual(0.5, result)