class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                # print (i, j, nums[i] + nums[j])
                if (nums[i] + nums[j] == target):
                    return [i, j]       
        return []