class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        new = 1
        old = 0

        while new < len(nums):
            if nums[new] == nums[old]:
                new = new + 1
            else:
                old = old+1
                nums[old] = nums[new]
                new = new + 1

        print(nums)
        return nums

v = Solution()
nums = [1,1,1,2,2,2,2,3,3,3,4,5,6,7,9]
v.removeDuplicates(nums)
