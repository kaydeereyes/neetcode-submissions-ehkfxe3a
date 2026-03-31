class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = dict()
        tDict = dict()

        for char in set(s):
            sDict[char] = s.count(char)
            tDict[char] = t.count(char)
        return sDict == tDict