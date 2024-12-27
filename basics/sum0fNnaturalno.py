# NORMAL WAY
# def sum(n):
    # summ =0
#     while n > 0:
#         summ += n
#         n -=1
#     return summ
# s = sum(-6)
# print(s)
# Recursion WAY
def sum(n):
    if n == 1:
        return 1
    else:
        s =n+ sum(n-1)
        return s
print(sum(3))

