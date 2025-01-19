## Notes
# 
# Classic Binary search algorithm
# array is sorted, so we can implement the stardard approach
# we will check the middle of the list, if this is correct, return
# if the target was higher, we check between the middle and top
# if lower than we check the bottom to middle
# implement this recursively, until the middle is the target, which is returned
# if the while loop is complete, without a return, then we return -1




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while high >= low:
            middle = (low+high)//2
            if target == nums[middle]:
                return middle
            elif target >= nums[middle]:
                low = middle + 1
            elif target <= nums[middle]:
                high = middle - 1
        return -1
        
    
        
