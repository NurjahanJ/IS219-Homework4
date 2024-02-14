"""Testing calculator operations"""
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test to check if addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test to check if subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test to check if multiply function works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test to check if division function works'''
    assert divide(2,2) == 1
    