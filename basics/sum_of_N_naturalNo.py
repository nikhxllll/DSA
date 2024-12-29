def sumodd(n):
    if n ==1:
        return 1
    
    return 2*n-1 + sumodd(n-1)
print(sumodd(10))


def summ(n):
    if n ==1:
        return 1
    s= n + summ(n-1)
    return s
print(summ(3))