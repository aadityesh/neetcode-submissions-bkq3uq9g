# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def inorder(self, root, ls):

        # if not root: return 

        # self.inorder(root.left, ls)
        # ls.append(root.val)
        # self.inorder(root.right, ls)

    def dfs(self, root, k):

        if not root: return None

        left = self.dfs(root.left, k)
       

        self.val += 1
        if self.val == k: 
            print(f"@@root: {root.val}")
            print(f"@@self: {self.val}")
            print(f"@@k: {k}")
            return root.val

        right = self.dfs(root.right, k)

        return left or right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # traversal = []
        # self.inorder(root, traversal)

        # return traversal[k-1]
        self.val = 0
        return self.dfs(root, k)
        