# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = []):
#         self.val = val
#         self.neighbors = neighbors
# # """


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        clones = {}
        return self.traverse(node, clones)

    def traverse(self, node: 'Node', clones: Dict[int, 'Node']) -> 'Node':
        if node in clones:
            return clones[node]

        cloned = Node(node.val, [])
        clones[node] = cloned

        for neighbor in node.neighbors:
            cloned_neighbor = self.traverse(neighbor, clones)
            cloned.neighbors.append(cloned_neighbor)

        return cloned
