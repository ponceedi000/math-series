from math_series.series import fibonacci

def test_fibonacci_9():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual

def test_fibonacci_15():
    expected = 610
    actual = fibonacci(15)
    assert expected == actual