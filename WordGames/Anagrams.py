import json

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
  
    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True
  
    def does_word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word 


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]

for word in words:
    trie.add_word(word)

# print(trie.does_word_exist("wait")) #True
# print(trie.does_word_exist("")) #True
# print(trie.does_word_exist("waite")) #False
# print(trie.does_word_exist("shop")) #True
# print(trie.does_word_exist("shoppp")) #False


class Anagrams:
    def __init__(self) -> None:
        # 6 nodes for 6 characters in the iphone version
        # self.node1 = None
        # self.node2 = None
        # self.node3 = None
        # self.node4 = None
        # self.node5 = None
        # self.node6 = None

        self.node1 = 'A'
        self.node2 = 'P'
        self.node3 = 'I'
        self.node4 = 'D'
        self.node5 = 'L'
        self.node6 = 'S'

        # Create complete graph with 6 nodes since chars can be matched in any way
        self.graph = {  self.node1 : [self.node2, self.node3, self.node4, self.node5, self.node6],
                        self.node2 : [self.node1, self.node3, self.node4, self.node5, self.node6],
                        self.node3 : [self.node2, self.node1, self.node4, self.node5, self.node6],
                        self.node4 : [self.node2, self.node3, self.node1, self.node5, self.node6],
                        self.node5 : [self.node2, self.node3, self.node4, self.node1, self.node6],
                        self.node6 : [self.node2, self.node3, self.node4, self.node5, self.node1]
                        }

    def dfs(self, start):
        visited, stack = [], [start] # ✅ Use list
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(self.graph[vertex] - set(visited)) # ✅ Convert to set()
        return visited

    def test(self):
        print(self.DFS(self.node1))



a = Anagrams()
a.test()
    # def DFS(self, start, visited=None):
    #     if visited is None:
    #         visited = set()
    #     visited.add(start)

    #     print(start)

    #     for next in self.graph[start]


    # def input_words(self) -> None:
    #     '''Get user input for words.'''
    #     # for practice use apidls
    #     s = '''_ _ _ _ _ _'''
