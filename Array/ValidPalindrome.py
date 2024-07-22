#solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s = s.upper()
        for char in s:
            if char.isalnum():
                s1 = s1 + char
        s2 = s1[::-1]
        return s1 == s2

#testcase
print(Solution().isPalindrome("abc"))
