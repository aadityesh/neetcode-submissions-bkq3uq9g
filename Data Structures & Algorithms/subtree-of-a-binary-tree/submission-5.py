# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # def isSameTree(self, p, q):

    #     if not p and not q: return True
    #     if not p and q: return False
    #     if not q and p: return False
    #     if p.val != q.val: return False

    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def serialized_preorder(self, root):
    
        if not root:
            return "##"

        return str("@" + str(root.val) +
               self.serialized_preorder(root.left) +
               self.serialized_preorder(root.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if not root: return False
        # curr = self.isSameTree(root, subRoot)
        # left = self.isSubtree(root.left, subRoot)
        # right = self.isSubtree(root.right, subRoot)

        # return curr or left or right
        s1 = self.serialized_preorder(root)
        s2 = self.serialized_preorder(subRoot)
        print(f"ls1: {s1}")
        print(f"ls2: {s2}")
        if s2 in s1: return True

        return False
        
        