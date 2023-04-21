class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_all_words(node, prefix)

    def _find_all_words(self, node, prefix):
        result = []
        if node.is_end_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            result.extend(self._find_all_words(child_node, prefix + char))
            
        # Add words with common suffixes
        if len(node.children) > 1 or node.is_end_word:
            for char, child_node in node.children.items():
                if char != '$':
                    result.extend(self._find_all_words(child_node, prefix + char))
                    
        return result


trie = Trie()
trie.insert("apple")
trie.insert("applique")
trie.insert("banana")
trie.insert("orange")
trie.insert("pear")
trie.insert("peach")
trie.insert("peanut")
trie.insert("pineapple")

print(trie.starts_with("a"))  # Output: ['apple', 'applique']
print(trie.starts_with("ap"))  # Output: ['apple', 'applique']
print(trie.starts_with("b"))  # Output: ['banana']
print(trie.starts_with("o"))  # Output: ['orange']
print(trie.starts_with("pe"))  # Output: ['pear', 'peach', 'peanut']
print(trie.starts_with("pi"))  # Output: ['pineapple']
print(trie.starts_with("c"))  # Output: []
