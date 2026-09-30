# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root, subRoot):
            if root is None and subRoot is None: return True
            if root and not subRoot : return False
            if subRoot and not root : return False
            if root.val == subRoot.val :
                left = isEqual(root.left, subRoot.left)
                right = isEqual(root.right, subRoot.right) 
                if right and left : return True
            return False

        if root is None and subRoot is None: return True
        if root and not subRoot : return False
        if subRoot and not root : return False
        if root.val == subRoot.val :
            left = isEqual(root.left, subRoot.left)
            right = isEqual(root.right, subRoot.right) 
            if right and left : return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        
        