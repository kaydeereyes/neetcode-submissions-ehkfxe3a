class Solution:
    def isAnagram(self, i, j):
        if len(i) != len(j):
            return False

        iDict = dict()
        jDict = dict()

        for char in set(i):
            iDict[char] = i.count(char)
            jDict[char] = j.count(char)
        return iDict == jDict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = list()
        for i in range(len(strs)):
            agroup = []
            for j in range(len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    agroup.append(strs[j])
            if agroup not in grouped: grouped.append(agroup)
        return grouped