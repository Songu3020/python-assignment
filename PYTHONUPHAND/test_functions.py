#import unittest

from unittest import TestCase
from function_class import number_is_prime

class TestClass(TestCase):
    
    def test_that_number_is_prime(self):
    
         
        is_prime= number_is_prime(7)
    
        self.assertTrue(is_prime)
    
    def test_that_number_is_not_prime(self):
    
         
        is_prime= number_is_prime(20)
    
        self.assertFalse(is_prime)

    def test_if_negative_number_is_prime(self):

        is_prime_ = number_is_prime(-11)

        assertTrue(is_prime)
    
    
