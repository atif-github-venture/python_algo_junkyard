# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
#
# Example 1:
#
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: nums = [7,8,9,11,12]
# Output: 1


diction = {}
nums = [3,4,-1,1,2] #2
# nums = [1,2,0] #3
# nums = [7,8,9,11,12] #1

for x in nums:
    if x not in diction:
        diction[x] = 1
    else:
        diction[x] += 1

i = 1
print(diction)
while i in diction.keys():
    print(i)
    i += 1
print(i)