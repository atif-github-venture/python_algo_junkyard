nums = [5, 7, 7, 8, 8, 10]
target = 8
first_index = -1
if target in nums:
    first_index = nums.index(target)
print(first_index)

last_index = -1
for x in range(first_index + 1, len(nums)):
    if (nums[x] == target):
        last_index = x

print(last_index)