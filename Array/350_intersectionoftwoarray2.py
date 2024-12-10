class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        dict = {}

        for elem in nums1:
            if elem in dict:
                dict[elem] +=1
            else:
                dict[elem] = 1
        for elem in nums2:
            if elem in dict and dict[elem] > 0:
                nums3.append(elem)
                dict[elem] -=1
        return nums3