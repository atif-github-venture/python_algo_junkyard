# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


soln = Solution()
assert soln.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, "failed"
assert soln.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, "failed"
