def gcdd(a,b):
    if b ==0:
        return a
    return gcdd(b,a % b)

    
print(gcdd(48,18))