# def fibo(n):
#     for i in range(0,n):
#         sum = i + (i +1)
#     return sum
# print(fibo(4))

def single(nums=[]):
    freq = {}

    for num in nums:
        if num in nums:
            freq[num] = freq.get(num,0) +1
            print(freq.items())
    
single([10,10,20,30,30,40,4])

