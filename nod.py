def f(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
a, b = int(input()), int(input())
