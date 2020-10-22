class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Trie()
            curr = curr.nodes[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)