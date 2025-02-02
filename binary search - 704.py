### Notes
# Classic binary search
# We will recursively check the middle of the array for our target
# if this is our number, we return, but likely it is bigger or smaller
# then we must check the appriotriate half, (greater or less than middle)
# repeat until our middle number is the target
# we can do this by initializing our left and right on the edge
# while right is bigger than left, we can campare to middle and adjust accordingly
# if our target is not in the loop, and nothing is returned, return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right >= left:
            mid = (right + left)//2
            if target == nums[mid]:
               return mid
            elif target > nums[mid]:
                left = mid + 1
            else: 
                right = mid - 1
        return -1
        
            
