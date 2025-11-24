class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in string:
                    if j - i > max_len:
                        max_len = j - i
                        string = []
                        break
                    else:
                        string = []
                        break
                string.append(s[j])
        return (max_len)


