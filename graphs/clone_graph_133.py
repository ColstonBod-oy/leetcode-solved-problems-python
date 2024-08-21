class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        clone_map = {}

        def dfs(node):
            if node in clone_map:
                return clone_map[node]

            copy = Node(node.val)
            clone_map[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)