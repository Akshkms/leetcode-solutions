# LeetCode Problem: 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for i, num in enumerate(nums):
            complement = target - num
            if not complement in seen:
                seen[num] = i
            else:
                return ([seen[complement], i])
 

s = Solution()
print(s)   
