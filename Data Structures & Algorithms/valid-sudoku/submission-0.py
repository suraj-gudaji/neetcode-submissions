class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = []
        col_set = []
        sq_set =[]
        
        for _ in range(9):
            row_set.append(set())
            
        for _ in range(9):
            col_set.append(set())
            
        for _ in range(9):
            sq_set.append(set())

        for i in range(9):
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                
                sq_index = (i // 3) * 3 + (j // 3)
                    
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in sq_set[sq_index]:
                    return False
                
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                sq_set[sq_index].add(board[i][j])
                
        return True