#!/usr/bin/python3

import pytest

def fizzBuzz(input_to_test):
    if input_to_test%3 == 0:
        return "Fizz"
    return ""
#if modulo 3==0
#if modulo 5==0
#if modulo 15==0
def test():
    assert fizzBuzz(1) == ""

def test_should_return_fizz_if_is_divisible_by_3():
    assert fizzBuzz(3) == "Fizz"

