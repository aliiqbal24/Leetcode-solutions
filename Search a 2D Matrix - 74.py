### NOTES
# Perform binary search on first column (left)
# find the column where either target is equal to or bigger than, but smaller than the next
# this is the column of your possible target
# so we perform binary search in this row
# when target is found, we return true
# if no target is found, we return false

class Solution:
    def searchMatrix(self, matrix, target):
       
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        low, high = 0, m - 1
        row = -1  
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if mid == m - 1 or matrix[mid + 1][0] > target:
                    row = mid
                    break
                else:
                    low = mid + 1
            else:
                
                high = mid - 1
        
        if row == -1:
            return False
        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
