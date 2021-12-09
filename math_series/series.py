def fibonacci(n):
  """
  rule out invalid numbers, anything < 0.
  BASE CASE:
  if n = 0 then return 0
  if n = 1 or 2 then return 1
  ----------------------------------------------------------------
  if n greater than 2, then return function(n-1) + function(n-2)
  check test for code results
  """
  if n < 0:
    print("invalid number")
  if n == 1:
    return 1
  if n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
  """
  similar to above but adjust the base case
  if n = 0 then return 2
  if n = 1 then return 1
  """
  if n == 0:
      return 2
  if n == 1:
    return 1
  else:
    return lucas(n-1) + lucas(n-2)


def sum_series(n, a=0, b=1):
  """
  similar to above but adjust the base case
  if n = 0 then return 2
  if n = 1 then return 1
  """
  if n == 0:
    return a
  if n == 1:
    return b
  if n == 2:
    return b
  elif n > 2:
    return sum_series(n-1, a, b) + sum_series(n-2, a, b)
    