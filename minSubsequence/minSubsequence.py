class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        c=[]
        while (sum(c) <= sum(nums)):
            c.append(nums.pop())
        return(c)
