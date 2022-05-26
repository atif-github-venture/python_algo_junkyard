# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'

s = "()"
# s = "()[]{}"
# s = "()[]{}[)"
# s = "()(]"


def valid_parentheses(str):
    ret = True
    for x in range(0, int(len(str)), 2):
        print(x)
        if str[x] == '(':
            if str[x + 1] != ')':
                ret = False
        if str[x] == '[':
            if str[x + 1] != ']':
                ret = False
        if str[x] == '{':
            if str[x + 1] != '}':
                ret = False
    return ret


print('done')

print(valid_parentheses(s))
