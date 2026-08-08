class Solution(object):
    def getConcatenation(self, nums):
            n = len(nums)
            nl = [0] * (2*n)
            for i in range(n):
                nl[i] = nums[i]
                nl[i+n] = nums[i]
            return nl

        