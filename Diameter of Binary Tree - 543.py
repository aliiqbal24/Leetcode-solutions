### Notes 
# The diameter has a relation to a nodes height,
# as each node has a diameter of the sum of the max height on its left and right
# we can recursive find the left and right height of each node using a DFS
# since we are Traversing the entire tree, once and only once, the time coplexity is O(N)
# we will initiallize the diameter as 0 if root exist 
# then we add the result of the highest diameter as well as + 1 for the root
# finally return the sum and this is our diameter



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
