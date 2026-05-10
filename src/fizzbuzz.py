def fizzbuzz(n: int) -> str:
    """Classic FizzBuzz: multiples of 3 -> 'Fizz', 5 -> 'Buzz', both -> 'FizzBuzz'."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)