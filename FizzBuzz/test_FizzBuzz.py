#!/usr/bin/python3

def fizzBuzz(input_to_test):
    if input_to_test%15==0:
        return "FizzBuzz"
    if input_to_test%3 == 0:
        return "Fizz"
    if input_to_test%5 == 0:
        return "Buzz"
    return ""

def test_return_empty_string_when_is_not_divisible():
    assert fizzBuzz(1) == ""

def test_should_return_fizz_if_is_divisible_by_3():
    assert fizzBuzz(18) == "Fizz"

def test_should_return_buzz_if_is_divisible_by_5():
    assert fizzBuzz(35) == "Buzz"

def test_should_return_fizzBuzz_if_is_divisible_by_15():
    assert fizzBuzz(45) == "FizzBuzz"