class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_shortest_prefix(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char in node.children:
                node = node.children[char]
                prefix += char
                if node.is_end_of_word:
                    return prefix
            else:
                break
        return word  # Return the original word if no prefix found

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search_shortest_prefix(words[i])
        
        return ' '.join(words)

# Example usage:
solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(solution.replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"

dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(solution.replaceWords(dictionary, sentence))  # Output: "a a b c"
