class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        sep = []
        i = 1
        
        while x!=0:
            sep.append(x%(10**i))
            x /=10
        print(sep)
        for i in range(len(sep)//2):
            print(sep[i], sep[-i-1])
            if sep[i]!=sep[-i-1]:
                return False
        return True
        
        