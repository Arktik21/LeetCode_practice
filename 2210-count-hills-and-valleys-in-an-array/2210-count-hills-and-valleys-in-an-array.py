class Solution(object):
    def countHillValley(self, nums):
        total_hw = 0
        prev = nums[0]
        cur = nums[1]
        for i in range(1, len(nums) - 1):
            if (nums[i] == prev):
                continue

            if (prev > cur) & (nums[i + 1] > cur) or (prev < cur) & (nums[i + 1] < cur):
                total_hw += 1
                prev = cur
            cur = nums[i+1]
            
        return total_hw