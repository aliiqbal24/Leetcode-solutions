### NOTES
# We can try a recursive top down approach 
# this can be done by switching left and right subtrees starting from the root
# the final case would be switch the subtrees of the final parent
# we can handle base/ edge case by adding if not root return None
# Function will iterate through whole list once so Big O(N)
# return the inverted tree



#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

