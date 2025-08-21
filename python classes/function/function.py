# what is funmction
'''
    A function is a block of code that only runs when it is called.
     You can pass data, known as parameters, into a function.
     A function can return data as a result.
'''
# types of functions
'''
    1. Built-in functions: These are functions that are already defined in Python, such as `print()`, `len()`, etc.
    2. User-defined functions: These are functions that you define yourself using the `def` keyword.
    3. Lambda functions: These are small anonymous functions defined using the `lambda` keyword.
'''
# user defined function
def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")
# calling the function
greet("Alice")

# function with return value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b    
# calling the function and storing the result
result = add(5, 3)
print("The sum is:", result)  # Output: The sum is: 8

# what is parameter and argument
'''
    Parameters are the variables listed inside the parentheses in the function definition.
    Arguments are the values that are passed to the function when it is called.
'''
# what is function definition
'''
    A function definition is a block of code that defines what the function does.
    It starts with the `def` keyword, followed by the function name and parentheses containing any parameters.  
    The function body is indented and contains the code that will be executed when the function is called.
'''
# function definition example
def multiply(x, y):
    """This function multiplies two numbers and returns the result."""
    return x * y    
# calling the function
result = multiply(4, 5)
print("The product is:", result)  # Output: The product is: 20

