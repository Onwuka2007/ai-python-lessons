"""
A decorator is a function that takes another function as an argument, extends or modifies its
behaviour and retur another new fn
"""

import functools

# 1. Define the decorator
def my_decorator(func):
    @functools.wraps(func) # Best practice: Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print("Something is happening BEFORE the function is called.")
        result = func(*args, **kwargs) # Executes the original function
        print("Something is happening AFTER the function is called.")
        return result
    return wrapper

# 2. Apply the decorator
@my_decorator
def greet(name):
    print(f"Hello, {name}!")

# 3. Call the function
greet("Alice")
