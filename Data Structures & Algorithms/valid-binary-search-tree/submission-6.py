# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, ls):

        if not root: return 

        self.inorder(root.left, ls)
        ls.append(root.val)
        self.inorder(root.right, ls)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        traversal = []
        self.inorder(root, traversal)

        n = len(traversal)
        for i in range(0, n - 1):

            if traversal[i] >= traversal[i+1]:
                return False

        return True



        
