def intSum (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid numerical format...")
    else:
        return a + b

"""
# Sum function tests:
print(intSum(4, 5)) # Should return 9.0
print(intSum(4.5, 5)) # Should return 9.5
print(intSum(4, 'a')) # Should launch an error
print(intSum(4, False)) # Should return 4.0
print(intSum(4, True)) # Should return 5.0
"""

def subtract (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid numerical format...")
    else:
        return a - b

"""
# Subtraction function tests:
print(subtract(5, 4)) # Should return 1.0
print(subtract(4.5, 5)) # Should return -0.5
print(subtract(4, 'a')) # Should launch an error
print(subtract(4, False)) # Should return 4.0
print(subtract(4, True)) # Should return 3.0
"""

def multiply (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid numerical format...")
    else:
        return a * b

"""
# Multiplication function tests:
print(multiply(5, 4)) # Should return 20.0
print(multiply(4.5, 5)) # Should return 22.5
print(multiply(4, 'a')) # Should launch an error
print(multiply(4, False)) # Should return 0.0
print(multiply(4, True)) # Should return 4.0
"""

def divide (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid numerical format...")
    else:
        return a / b

"""
# Divide function tests:
print(divide(5, 1)) # Should return 5.0
print(divide(20, 1.0)) # Should return 20.0
print(divide(4, 'a')) # Should launch an error
print(divide(4, False)) # Should return a float division error
print(divide(4, True)) # Should return 4.0
"""