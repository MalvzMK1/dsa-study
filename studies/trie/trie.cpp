#include <unordered_map>
#include <string>
#include <iostream>

class TrieNode {
public:
  std::unordered_map<char, TrieNode> _children;
  bool _is_end_of_word;

  TrieNode() {
    _is_end_of_word = false;
  }
};

class Trie {
private:
  TrieNode _root;
public:
  Trie(): _root(TrieNode()) {}

  void insert(const std::string& word) {
    // this does not work cause it creates a new object instead of referencing the existent object
    // TrieNode currentNode = _root;
    TrieNode* currentNode = &_root;
    for (const char& ch: word ) {
      if (!currentNode->_children.count(ch)) {
        currentNode->_children[ch] = TrieNode();
      }
      currentNode = &currentNode->_children[ch];
    }
    currentNode->_is_end_of_word = true;
  }

  bool starts_with(const std::string& prefix) {
    auto currentNode = &_root;
    for (const char& ch: prefix ) {
      if (!currentNode->_children.count(ch)) {
        return false;
      }
      currentNode = &currentNode->_children[ch];
    }
    return !currentNode->_is_end_of_word;
  }

  bool search(const std::string& word) {
    auto currentNode = &_root;
    for (const char& ch: word ) {
      if (!currentNode->_children.count(ch)) {
        return false;
      }
      currentNode = &currentNode->_children[ch];
    }
    return currentNode->_is_end_of_word;
  }
};

int main() {
  Trie trie;
  std::string word = "banana";
  trie.insert(word);

  std::cout << "Word: " << word << std::endl << std::endl;

  std::cout << "Starts With ban? " << trie.starts_with("ban") << std::endl;
  std::cout << "Starts With bane? " << trie.starts_with("bane") << std::endl;

  std::cout << std::endl;

  std::cout << "Search for banana: " << trie.search("banana") << std::endl;
  std::cout << "Search for pneumoultramicroscopicossilicovulcanoconiotico: " << trie.search("pneumoultramicroscopicossilicovulcanoconiotico") << std::endl;
}
