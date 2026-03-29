# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root, traversal):

        if not root: 
            traversal.append(-101)
            return

        traversal.append(root.val)
        self.preorder(root.left, traversal)
        self.preorder(root.right, traversal)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # if p is None and q is None: return True
        # if p is None and q: return False
        # if q is None and p: return False
        # if p.val != q.val: return False

        # left = self.isSameTree(p.left, q.left)
        # right = self.isSameTree(p.right, q.right)

        # if left and right: 
        #     return True 
        
        # return False

        p_traversal = []
        q_traversal = []

        self.preorder(p, p_traversal)
        self.preorder(q, q_traversal)
        print(p_traversal)
        print(q_traversal)
        # print(p)
        return p_traversal == q_traversal
        



     