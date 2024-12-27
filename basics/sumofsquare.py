def square(n):
    if n == 1:
        return 1
    else:
        return n*n + square(n-1)
print(square(5))