class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        l = 0
        r = n-1
        arr = [0]*n
        k = n-1
        while(l<=r):
            if abs(nums[l])<abs(nums[r]):
                arr[k] = nums[r] ** 2
                r-=1
            else:
                arr[k] = nums[l] ** 2
                l +=1
            k -=1
        return arr