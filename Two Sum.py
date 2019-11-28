"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            i += 1
        return 'No solution to this problem.'

    class Solution(object):

    
    def twoSum_(self,nums,target):
        d={}
        #keys are index of the original list, values are list items
        for i in range(len(nums)):
            d[i]=nums[i]
            d_keys=sorted(d,key=lambda i:nums[i])
            
        lower=0
        upper=len(d_keys)-1
        while lower<upper:
            if d[d_keys[lower]]+d[d_keys[upper]]==target:
                return [d_keys[lower],d_keys[upper]]
            elif d[d_keys[lower]]+d[d_keys[upper]]>target:
                upper+=-1
            else:
                lower+=1
        return 'No solution to this problem'
