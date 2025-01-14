# notes
# in programing, we can remove duplicates by making a set
# if our array nums has the same length after it is made to a set
# then we know that it contained no duplictes
# so by comparing lengths we know if there was a duplicate
# this is checked in negation and returned

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(nums) != len(s)
