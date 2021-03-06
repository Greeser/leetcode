# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root==None:
            return 0
        
        if root.val == R and root.val == L:
            return 1
        
        if root.val <= R and root.val >= L:
            return (root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L,R))
        
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        
        else:
            return self.rangeSumBST(root.left, L, R)
