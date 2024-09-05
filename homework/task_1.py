# Task: Represent common single-variable mathematical functions in Python.

# 1. Define a function called linear_function that represents the linear function f(x) = 2x+3.
  def linear_function(x):
    f = 2(*x)+3
    return f


# 2. Define a function called constant_function that represents the constant function g(x) = 4.
    def constant_function(x):
      g = 4
      return g


# 3. Define a function called exponential_function that represents the exponential function h(x) = 2^x.
  def exponential_function(x):
      h = 2**x
      return h


# 4. Use a built-in command to define a function called absolute_value that represents the absolute value function k(x)=|x|.
    def absolute_value(x):
      if x > 0:
        return x
      else:
        return -1*x

