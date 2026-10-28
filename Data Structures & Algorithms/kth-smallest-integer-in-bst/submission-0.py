
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return False

            if dfs(node.left) : return True
            values.append(node.val)
            if len(values) == k: return True
            if dfs(node.right): return True
            return False

        dfs(root)

        return values[-1]
