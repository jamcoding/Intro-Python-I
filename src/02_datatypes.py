"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# convert integer to string
x_str = str(x)

# convert string to integer
y_int = int(y)

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
print(x + int(y))
print(x + y_int)


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
print(f'{x}{y}')
print(x_str + y)