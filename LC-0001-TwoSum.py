# LeetCode Problem: 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for i, num in enumerate(nums):         # Loop with nums.items() with index "i" and "nums"   
            find_num = target - num            # Calculate what we need
            if find_num in seen:               # If find_num difference exists
                return [seen[find_num], i]     # Return immediately
            else:                              # If not found
                seen[num] = i                  # Save current number in seen array
 
            


s = Solution()
print(s)   
