class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        total_len = len(nums)
        if total_len % 2 == 0:
            return (nums[total_len // 2 - 1] + nums[total_len // 2]) / 2.0
        else:
            return nums[total_len // 2]