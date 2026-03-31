class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        row = defaultdict(set)
        squares = defaultdict(set)

        for r in range (9):
            for c in range (9):
                position = board[r][c]
                if position == '.':
                    continue
                if (position in row[r] or position in cols[c] or position in squares[(r // 3 , c // 3)]):
                    return False

                cols[c].add(position)
                row[r].add(position)
                squares[(r // 3, c // 3)].add(position)

        return True



        
        