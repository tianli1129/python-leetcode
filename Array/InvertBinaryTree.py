from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        #actual swapping
        root.left = right
        root.right = left
        return root

#testcase
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = right
root.right = left
res = Solution().invertTree(root)
