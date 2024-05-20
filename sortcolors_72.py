#Leetcode Problem 72. Sort colors. 
#See: https://leetcode.com/problems/sort-colors/description/
#Given an array with n objects colored red, white, blue, sort them in-place so that objects of the
#same color are adjacent, with the colors in the order red, white, blue.
# 0 = red, 1 = white, 2 = blue


#Note: This funciton implements bucket sort, for 0(n) time (O(n) time still holds given the nested loop).
def sort_array(arr):

    c = [0,0,0] #this is the counts of red, white, blue, respectively
    for val in arr:
        c[val] += 1

    k = 0
    for i in range(0,len(c)):
        for j in range(0,c[i]):
            arr[k] = i
            k += 1

    return arr


a = [0,1,1,1,0,2,0,0,2]
print(sort_array(a))
