class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = s.split()
        slast = slist[-1]
        n = len(slast)
        return n
