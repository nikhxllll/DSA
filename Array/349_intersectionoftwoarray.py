class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        seen = set(nums1)

        for n in nums2:
            if n in seen:
                nums3.append(n)
                seen.remove(n)

        return nums3