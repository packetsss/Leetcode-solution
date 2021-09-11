# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Regular recursive solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return 1 + max(l, r)
        return 0

# One liner
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))