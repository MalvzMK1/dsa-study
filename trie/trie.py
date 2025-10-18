class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def starts_with(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return not current_node.is_end_of_word

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.is_end_of_word

    def get_possible_words(self, prefix: str) -> list[str]:
        current_node = self.root
        words = []

        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]

        previous_chars = []

        def dfs(node: TrieNode, previous_chars):
            if node.is_end_of_word:
                words.append(prefix + ''.join(previous_chars))

            for child in node.children:
                previous_chars.append(child)
                dfs(node.children[child], previous_chars)
                previous_chars = []

        dfs(current_node, previous_chars)

        return words


if __name__ == "__main__":
    trie = Trie()

    trie.insert('banana')
    trie.insert('barista')
    trie.insert('bar')
    trie.insert('balde')
    trie.insert('bana')
    trie.insert('barco')

    words = trie.get_possible_words('bar')

    print(words)

