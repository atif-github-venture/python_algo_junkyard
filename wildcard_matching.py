# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Example 1:
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = True
        if (len(s) > len(p) and p != '*') or (len(s) < len(p)):
            result = False
        elif p == '*':
            pass
        else:
            x = list(s)
            y = list(p)
            siz = len(y)
            for i in range(siz):
                if (y[i] == x[i]) or (y[i]) == '?':
                    continue
                else:
                    result = False
        return result


a = Solution()
print(a.isMatch("aa", "a"))
print(a.isMatch("aa", "*"))
print(a.isMatch("cb", "?a"))
print(a.isMatch("cb", "?b"))
print(a.isMatch("cbz", "?b?"))
