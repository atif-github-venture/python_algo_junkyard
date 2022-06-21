# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            index = 0
            search_len = len(nums)
            while search_len != 0:
                if nums[len(nums) - 1] < target:
                    return len(nums)
                if nums[index] > target:
                    return index
                index += 1
                search_len -= 1


soln = Solution()
print(soln.search_insert([1, 3, 5, 6], 5))
print(soln.search_insert([1, 3, 5, 6], 2))
print(soln.search_insert([1, 3, 5, 6], 7))
print(soln.search_insert([1, 3, 5, 7], 6))
print(soln.search_insert([1, 3, 5, 7], 4))

