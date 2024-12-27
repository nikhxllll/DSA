def reversee(n):
    if n > 0:
        print(n,end = " ")
        r = reversee(n-1)
rr = reversee(10)
print(rr)