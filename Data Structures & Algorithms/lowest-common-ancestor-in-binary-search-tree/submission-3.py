# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getHeight(self, dists, node):
        curr = node
        res = 0
        while curr is not None:
            curr = dists[curr]
            res +=1
        return res
         
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(root)
        required = set([p.val, q.val])
        dist = {root:None}
        found = []
        to_remove = set()
        while required:
            curr_node = queue.pop()
            val = curr_node.val
            for v in required:
                if v < val:  
                    if curr_node.left: 
                        dist[curr_node.left] = curr_node
                        queue.append(curr_node.left)
                elif v > val: 
                    if curr_node.right:
                        dist[curr_node.right] = curr_node
                        queue.append(curr_node.right)
                else:
                    to_remove.add(curr_node.val)
                    found.append(curr_node)
            required = required.difference(to_remove)
        
        dist1 = self.getHeight(dist, found[0])
        dist2 = self.getHeight(dist, found[1])
        while(found[0] != found[1]):
            if dist1>=dist2: 
                dist1 -= 1
                found[0] = dist[found[0]]
            else:
                dist2 -= 1
                found[1] = dist[found[1]]
        return found[0]

        

                    
                        
                




        