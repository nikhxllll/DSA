def printt(nums,idx=0):
    if idx == len(nums):
        return
    print(nums[idx])
    printt(nums,idx+1)

lists = [10,20,30,40]
printt(lists)

