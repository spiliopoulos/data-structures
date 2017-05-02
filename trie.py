class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = 0
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
        node.freq += 1

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
        return (node.freq > 0) and (not suffix)

    def frequency(self, word):
        """
        Returns the times the word was added in the trie
        :type word: str
        :rtype: bool
        """
        node, suffix = self._return_last_included_node(word)
        if suffix:
            return 0
        else:
            return node.freq

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        _, suffix = self._return_last_included_node(prefix)
        #print(suffix)
        return (not suffix)
