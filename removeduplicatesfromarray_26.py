class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        curr = 0
        sweep = 0

        while sweep < len(nums):
            if nums[sweep] == val:
                sweep += 1
            else:
                nums[curr] = nums[sweep]
                curr += 1
                sweep += 1
        print(curr)
        print(nums)


v = Solution()
s = [0,1,0,0,2,1,1,0]
v.removeElement(s,0)
