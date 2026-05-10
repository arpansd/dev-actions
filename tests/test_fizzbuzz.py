from src.fizzbuzz import fizzbuzz

def test_returns_number_when_no_match():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_fizz_for_multiples_of_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_buzz_for_multiples_of_five():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(25) == "Buzz"

def test_fizzbuzz_for_multiples_of_fifteen():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"