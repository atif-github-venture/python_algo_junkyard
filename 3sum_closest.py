# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:
#
# Input: nums = [0,0,0], target = 1
# Output: 0

# Input: arr[] = {-1, 2, 1, -4}, X = 1
# Output: 2
# Explanation:
# Sums of triplets:
# (-1) + 2 + 1 = 2
# (-1) + 2 + (-4) = -3
# 2 + 1 + (-4) = -1
# 2 is closest to 1.
#
# Input: arr[] = {1, 2, 3, 4, -5}, X = 10
# Output: 9
# Explanation:
# Sums of triplets:
# 1 + 2 + 3 = 6
# 2 + 3 + 4 = 9
# 1 + 3 + 4 = 7
# ...
# 9 is closest to 10.
import sys
from itertools import combinations

nums = [-1, 2, 1, -4]
target = 1
closestSum = sys.maxsize
final = combinations(nums, 3)
for x in final:
    if abs(target - closestSum) > abs(target - sum(x)):
        closestSum = sum(x)

print('done')


