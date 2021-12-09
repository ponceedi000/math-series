def fibonacci(n):
  """
  rule out invalid numbers, anything < 0.
  if n = 0 then return 0
  if n = 1 or 2 then return 1
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


# def lucas(n):
#   """
#   sdf
#   """
#   pass