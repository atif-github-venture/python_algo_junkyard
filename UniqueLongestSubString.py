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


ulss = UniqueLongestSubString('abcabcbb')
# ulss = UniqueLongestSubString('bbbbb')
# ulss = UniqueLongestSubString('pwwkew')
print(ulss.longest_string())