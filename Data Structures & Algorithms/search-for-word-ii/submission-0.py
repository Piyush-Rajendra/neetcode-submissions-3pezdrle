class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def addWord(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        rows, cols = len(board),  len(board[0])
        result = []

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "#":
                return
            ch = board[r][c]
            if ch not in node.children:
                return

            nextNode = node.children[ch]

            if nextNode.word is not None:
                result.append(nextNode.word)
                nextNode.word = None

            board[r][c] = '#'
            dfs(r + 1, c, nextNode)
            dfs(r - 1, c, nextNode)
            dfs(r, c + 1, nextNode)
            dfs(r, c - 1, nextNode)
            board[r][c] = ch

            if not nextNode.children and nextNode.word is None:
                del node.children[ch]

        for r in range (rows):
            for c in range (cols):
                dfs(r, c, root)

        return result
