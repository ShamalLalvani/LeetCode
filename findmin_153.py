#Leetcode 153. Find Minimum in Rotated Sorted Array.
#   Problem: Suppose an array of length n sorted in ascending order is rotated
#   between 1 and n times. (i.e. a cyclic rotation)
#   Given the sorted rotated array nums of unique elements, return the
#   minimum element of this array in 0(log n) time.



def returnMinimum(nums):


    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums[0],nums[1])
    else:
        ind = len(nums) // 2 # find the midpoint
        print(ind,len(nums)-1)

        if nums[ind] > nums[ind+1]:
            return nums[ind+1]
        else:
            return returnMinimum(nums[0:ind+1])




s = [4,5,7,22,1,3]
v = returnMinimum(s)
print(v)
