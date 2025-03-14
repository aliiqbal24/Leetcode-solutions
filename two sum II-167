# notes
# increasing order array
# left smallest number, right biggest
# always a valid solution
# We want a constant use of addition space
# by using 2 pointers, left and right, we can check if sum matches targets
# if equal return index +1, likely will be bigger or smaller than target
# if smaller, move left pointer up one
# if bigger move smaller output down one
# continue until they balance to make the sum - can be done with recursion

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right = len(numbers)-1
        left = 0

        while left < right: 
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1,right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1 
                





