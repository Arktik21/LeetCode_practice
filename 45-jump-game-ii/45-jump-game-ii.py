class Solution(object):
    def jump(self, nums):
        s,e=0,0
        ans=0
        while(e<len(nums)-1):
            end=0
            for i in range(s,e+1):
                end=max(end,i+nums[i])
            s=e+1
            e=end
            ans+=1
        return ans
        