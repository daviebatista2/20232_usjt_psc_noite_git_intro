def intSum (a, b):
    a = float(a)
    b = float(b)

    if (type(a) != float or type(b) != float):
        print("One of the parameters is not on a valid integer format...")
    else:
        return a + b