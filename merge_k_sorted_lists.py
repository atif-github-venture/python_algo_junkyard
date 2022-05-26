# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
import numpy as np


class Solution:
    def mergeKLists(self, lists):
        res = []
        if len(lists) != 0:
            if type(lists) == dict:
                arr = []
                for x in lists.values():
                    arr.append(x)
                lists = arr
            elif type(lists) == list:
                pass
            res = np.concatenate(lists)
            res.sort()
        return res


lis = [[1, 4, 5], [1, 3, 4], [2, 6]]


# lis = {
#     1: [1, 4, 5],
#     2: [1, 3, 4],
#     3: [2, 6]
# }
# lis = []
# lis = [[]]
sol = Solution()
print(sol.mergeKLists(lis))
