def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

def factt(n):
    temp = 1
    while n > 0:
        temp *= n
        n -=1
    return temp
print(factt(0))