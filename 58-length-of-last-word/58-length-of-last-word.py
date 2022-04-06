class Solution(object):
    def lengthOfLastWord(self, s):
        k  = 0
        for i in reversed(range(len(s))):
            if (s[i] == ' ') & (k!=0):
                return k
            if s[i]!=' ':
                k+=1
                
            if i == 0:
                return k