

class Solution:

    def with_binary_search(self, nums, low, high, x):
        mid = (high + low) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return self.with_binary_search(nums, low, mid - 1, x)
        else:
            return self.with_binary_search(nums, mid + 1, high, x)


soln = Solution()
arr = [1, 3, 5, 6]
target = 5
# target = 6
print(soln.with_binary_search([1, 3, 5, 6], 0, len(arr) - 1, target))