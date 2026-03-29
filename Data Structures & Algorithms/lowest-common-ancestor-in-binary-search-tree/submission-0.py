# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def find_path(self, root, p, ls):
        if not root: return False

        ls.append(root)

        if root.val == p.val: return True
        if self.find_path(root.left, p, ls) or self.find_path(root.right, p, ls): return True

        ls.pop()
        return False;


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        path_p = []
        path_q = []

        self.find_path(root, p, path_p)
        self.find_path(root, q, path_q)

        res = None

        length = min(len(path_p), len(path_q))

        for i in range(0, length):
            if path_p[i].val == path_q[i].val: 
                res = path_p[i]
            else: 
                break
        
        return res

        