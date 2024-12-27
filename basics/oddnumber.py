def oddno(n):
    if n > 0:
        oddno(n-1)
        print(2*n-1,end = " ")
oddno(11)