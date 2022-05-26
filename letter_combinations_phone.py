# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# digits = '234'
# import itertools
# arr = []
# for x in digits:
#     arr.append(phone[x])
# comb = list(itertools.product(arr[0], arr[1]))
# print(comb)

# googled solution

class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        characters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = []
        self.solve(digits, characters, result)
        return result

    def solve(self, digits, characters, result, current_string="", current_level=0):
        if current_level == len(digits):
            result.append(current_string)
            return
        for i in characters[int(digits[current_level])]:
            self.solve(digits, characters, result, current_string + i, current_level + 1)


ob1 = Solution()
print(ob1.letterCombinations("234"))
