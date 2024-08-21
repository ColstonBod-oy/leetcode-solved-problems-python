class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.res = float("-inf")  

        def postOrder(node):
            if not node:
                return 0

            maxLeft = max(postOrder(node.left), 0)
            maxRight = max(postOrder(node.right), 0)

            self.res = max(self.res, maxLeft + node.val + maxRight)
            return max(maxLeft, maxRight) + node.val

        postOrder(root)
        return self.res
        