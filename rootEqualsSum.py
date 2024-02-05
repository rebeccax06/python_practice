#leet code 2236: You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
#Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        if root.left.val + root.right.val == root.val:
            return True
        else:
            return False
# Test cases
root1 = TreeNode(10, TreeNode(4), TreeNode(6))
sol = Solution()
print(sol.checkTree(root1))  # Expected output: True

# Case 2: Invalid tree
root2 = TreeNode(5, TreeNode(3), TreeNode(1))
print(sol.checkTree(root2))  # Expected output: False

# Case 3: Empty tree
empty_tree = None
print(sol.checkTree(empty_tree))  # Expected output: True