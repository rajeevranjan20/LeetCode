# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        vals, l = [], [root]
        while l:

            n = l.pop(0)
            vals.append(n.val)
            if n.right: l = [n.right] + l    
            if n.left: l = [n.left] + l        
        return vals       
        