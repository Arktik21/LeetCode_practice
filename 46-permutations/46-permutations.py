class Solution(object):
    def permute(self, nums):
        
        n = len(nums)
        if n==0:
            return [[]]
        if n==1:
            return [nums]
        
        permutations = self.permute(nums[:n-1])
         
        ret_list = [None]*math.factorial(n)
        i=0
        
        for perm in permutations:
            for x in range(n):
                ret_list[i] = perm[:x] + [nums[n-1]] + perm[x:]
                i += 1        
        return ret_list