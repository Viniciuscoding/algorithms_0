"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# SOLUTION by lee215
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        front, back = nums, nums[::-1]
        
        for i in range(1,len(nums)):
            front[i] = front[i] * (front[i-1] or 1)
            back[i] = back[i] * (back[i-1] or 1)

        return max(front + back)
