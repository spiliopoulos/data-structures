class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.nexts = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node, suffix = self._return_last_included_node(word)
        for char in suffix:
            new_trie = Trie()
            node.nexts[char] = new_trie
            node = new_trie
        node.end = True

    def _return_last_included_node(self, word):
        node = self
        for i, char in enumerate(word):
            #print(char)
            if not char in node.nexts:
                return (node, word[i:])
            node = node.nexts[char]
        return (node, [])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node, suffix = self._return_last_included_node(word)
        return node.end and (not suffix)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        _, suffix = self._return_last_included_node(prefix)
        #print(suffix)
        return (not suffix)
