def intSum (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid integer format...")
    else:
        return a + b

print(intSum(4, 5)) # Should return 9.0
print(intSum(4.5, 5)) # Should return 9.5
print(intSum(4, 'a')) # Should launch an error
print(intSum(4, False)) # Should return 4.0
print(intSum(4, True)) # Should return 5.0