def removeDuplicates(nums):
    """
    :type nums: List[int],in order
    :rtype: int
    """
    nums_new = []
    count = 0
    for i in nums:
        if i not in nums_new:
            nums_new.append(i)
            count += 1
    nums = nums_new[:]
    return count,nums

nums1=[1,1,2,2,3,3,3,4]
nums2=[2,2,2,2]
nums3=[1,2,3,4]

numss=[nums1,nums2,nums3]

for nums in numss:
    print(removeDuplicates(nums))