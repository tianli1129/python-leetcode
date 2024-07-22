class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t

print(Solution().isAnagram("abc","cba"))       