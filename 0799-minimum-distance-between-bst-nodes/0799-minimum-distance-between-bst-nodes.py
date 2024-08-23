# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res=[]
        def helper(node):
            if node is not None:
                res.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        res=sorted(res)
        temp=float('inf')
        print(res)
        for i in range(1,len(res)):
            temp=min(temp,abs(res[i-1]-res[i]))
        return temp
                