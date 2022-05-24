# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6
nums = [3, 3]
target = 6

from more_itertools import locate

pos1 = pos2 = None
for i in nums:
    res = target - i
    if res in nums:
        if target / 2 != target - i:
            pos1 = nums.index(res)
            pos2 = nums.index(i)
        else:
            all_index = list(locate(nums, lambda x: x == res))
            all_index.pop()
            pos1 = all_index[0]
            pos2 = nums.index(i)
print(pos1, ' & ', pos2)
print('done')
