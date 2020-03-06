# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        result = []
        self.preorder_serialize(root, result)

        return ",".join(result)

    def preorder_serialize(self, root, result):
        if root is None:
            result.append("None")
            return

        result.append(str(root.val))
        self.preorder_serialize(root.left, result)
        self.preorder_serialize(root.right, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        data_list = data.split(",")
        return self.preorder_deserialize(data_list)

    def preorder_deserialize(self, data):
        if len(data) == 0:  # Just for sanity check, but not necessary
            return None

        val = data.pop(0)

        if val == "None":
            return None

        node = TreeNode(int(val))
        node.left = self.preorder_deserialize(data)
        node.right = self.preorder_deserialize(data)

        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
