# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


def common_prefix_util(list_a, list_b):
    match_list = []
    for j in range(min(len(list_a), len(list_b))):
        if list_a[j] == list_b[j]:
            match_list.append(list_a[j])
    return match_list


def is_present(index, str_to_find, list_a):
    for x in list_a:
        if str_to_find != x[index]:
            return False
    return True


# a = ["dog","racecar","car"]
a = ["flower", "flow", "flight"]
a = sorted(a, key=len)
# a = ["dog", "racecar", "car"]
pref = a[0]
str = ''
for i in range(len(a[0])):
    str_to_find = a[0][i]
    if is_present(i, str_to_find, a):
        str += str_to_find
print(str)
