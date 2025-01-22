# Notes
# target == 0 every time, numbers are not ordered
# Brute for would be 3 nested for loops, with O(n^3) time complexity
#APPROACH 1 
# We can sort the array in O(nlogn)
# there can be many solutions
# we can start by sorting the array
# with a sorted array we can iterate each number, skipping duplicates
# now we can use two pointers at the left and right
# check if the target is matched, if so store and continue
# if not adjust the left or right, according to is the target is <,>
# return all results




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
