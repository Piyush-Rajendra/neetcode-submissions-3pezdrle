class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols= len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, index):
        #base cases
        if index == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if word[index] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = 'visited'

        found = (self.dfs(board, word, i-1, j, index + 1) or 
                self.dfs(board, word, i+1, j, index + 1 )or
                self.dfs(board, word, i,j-1, index + 1)or
                self.dfs(board, word, i,j+1, index + 1))
        
        board[i][j] = tmp

        return found