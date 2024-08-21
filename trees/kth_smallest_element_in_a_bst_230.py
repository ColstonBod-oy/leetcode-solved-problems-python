class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.count = k
        self.result = None
        def inOrder(node):
            if not node or self.result is not None:
                return
            
            inOrder(node.left)
            self.count -= 1
            if self.count == 0:
                self.result = node.val
                return
            inOrder(node.right)
            
        inOrder(root)
        return self.result