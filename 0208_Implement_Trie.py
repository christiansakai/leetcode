class Trie:
    class Node:
        def __init__(self, val: str):
            self.val = val
            self.is_word = False
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for i in range(0, len(word)):
            ch = word[i]

            if ch in node.children:
                if i == len(word) - 1:
                    node.children[ch].is_word = True
            else:
                if i == len(word) - 1:
                    node.children[ch] = self.Node(ch, True)
                else:
                    node.children[ch] = self.Node(ch, False)

            node = node.children[ch]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for i in range(0, len(word)):
            ch = word[i]

            if not(ch in node.children):
                return False

            if i == len(word) - 1:
                return node.children[ch].is_word

            node = node.children[ch]

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for ch in prefix:
            if not(ch in node.children):
                return False

            node = node.children[ch]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
