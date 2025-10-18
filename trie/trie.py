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


if __name__ == "__main__":
    trie = Trie()

    word = input('Word: ')
    trie.insert(word)

    word = input('Search: ')
    print(trie.search(word))

    word = input('Starts With: ')
    print(trie.starts_with(word))



