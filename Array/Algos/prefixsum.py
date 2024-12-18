# Prefix sum algo done by me

def prefix(nums):
    p = []

    for i in range(len(nums)):  # we can avoid if and else condition by checking for loop with 1 ,len(nums)
        if i > 0:
            nums[i] += nums[i-1]
            p.append(nums[i])
        else:
            nums[i] = nums[i]
    return p


l = [10,20,30,40,50]
s = [1219,1232,424124,24124,]
prefix(s)



print(s)