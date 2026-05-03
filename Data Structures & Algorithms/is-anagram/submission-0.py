class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char not in sChars:
                sChars[char] = 1
            else:
                sChars[char] += 1

        for char in t:
            if char not in tChars:
                tChars[char] = 1
            else:
                tChars[char] += 1

        return sChars == tChars;