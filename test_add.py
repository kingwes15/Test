import calculator   # The code to test

def test_add():
    assert calculator.add(3,1) == "3 + 1 = 4"

# This test is designed to fail for demonstration purposes.
def test_subtract():
    assert calculator.subtract(3,1) == "3 - 1 = 2"

def test_multiply():
    assert calculator.multiply(3,9) == "3 * 9 = 27"

def test_divide():
    assert calculator.divide(3,3) == "3 / 3 = 1.0"

def test_exponent():
    assert calculator.exponent(3,3) == "3^3 = 27"