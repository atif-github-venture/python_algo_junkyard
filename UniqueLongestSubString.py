class UniqueLongestSubString:
    def __init__(self, str):
        self.string = str

    def longest_string(self):
        ans = 0
        for i in range(len(self.string)):
            for j in range(i + 1, len(self.string)):
                if self.is_unique(self.string, i, j):
                    ans = max(ans, j - i)
        return ans

    def is_unique(self, str, start, end):
        setm = set()
        for k in range(start, end):
            ch = str[k]
            if ch in setm:
                return False
            else:
                setm.add(ch)
        return True


# ulss = UniqueLongestSubString('abcabcdbb')
# print(ulss.longest_string())

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


# a = ["flower", "flow", "flight"]
# a = sorted(a, key=len)
# # a = ["dog", "racecar", "car"]
# pref = a[0]
# str = ''
# for i in range(len(a[0])):
#     str_to_find = a[0][i]
#     if is_present(i, str_to_find, a):
#         str += str_to_find
# print(str)
#
# x = [0,1,2,2,3,0,4,2]
# num = 2
# # x = list(y for y in x if y != num)
#
# x = list(filter(lambda y: (y!=num), x))
# print(x)

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# first_index = -1
# if target in nums:
#     first_index = nums.index(target)
# print(first_index)
#
# last_index = -1
# for x in range(first_index + 1, len(nums)):
#     if (nums[x] == target):
#         last_index = x
#
# print(last_index)

# fill in the missing numbers
x = [3, 4, -1, 1]

x.sort()
print(x)
y = list(z for z in range(x[0], x[len(x)-1]))
print(y)
