# notes
# We want 2 seperate indexing when, added together equal target
# can be brute forced by checking each comibination but we can do better
# we can iterate through the array, storing each value, or what it
# needs to reach the target, and as we keep going, we can do a check
# to see if the sum is formable
# this is worst case O(n)

class Solution:
    def twoSum(self, nums, target):
        checked = {}  # Value: Index

        for i in range(len(nums)):
            difference = target - nums[i]  
            if difference in checked: 
                return [checked[difference], i]
            else:
                
                checked[nums[i]] = i

        
        return []
