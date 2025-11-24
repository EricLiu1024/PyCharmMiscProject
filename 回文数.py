class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        flag = True
        for i in range(len(x_str)):
            if x_str[i] != x_str[len(x_str) - 1 - i]:
                flag = False
                break
        return (flag)

