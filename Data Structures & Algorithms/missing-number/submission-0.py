class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        for i in range(n):
            if nums[i] != i:
                return i
        return n
        