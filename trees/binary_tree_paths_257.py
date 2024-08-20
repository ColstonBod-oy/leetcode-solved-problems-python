class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        
        def preOrder(root, current_path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(current_path + str(root.val))

            preOrder(root.left, current_path + str(root.val) + "->")
            preOrder(root.right, current_path + str(root.val) + "->")
        preOrder(root, "")
        return res
            