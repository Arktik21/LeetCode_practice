class Solution(object):
    
    def getCount(self, nums):
        count = {}
        for i in nums:
            if i not in count:
                count[i] = True
        return count
    
    def findDifference(self, nums1, nums2):

        count1 = self.getCount(nums1)
        count2 = self.getCount(nums2)
        nums1 = []
        for i in count1:
            if i not in count2:
                nums1.append(i)
        nums2 = []
        for i in count2:
            if i not in count1:
                nums2.append(i)
        
        return [nums1, nums2]
	


	