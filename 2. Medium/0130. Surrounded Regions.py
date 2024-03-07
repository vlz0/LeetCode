class Solution:

    def solve(self, board: List[List[str]]) -> None:
        n_rows, n_cols = len(board), len(board[0])

        # all "O"s in the border are unsurrounded, we find these, then traverse adjacent "O"s
        def dfs(r, c):
            if r < 0 or r == n_rows or c < 0 or c == n_cols or board[r][c] != "O":
                return
          
            board[r][c] = "T" # these are unsurrounded
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O" and (r in [0, n_rows - 1] or c in [0, n_cols - 1]):
                    dfs(r, c)

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O": # surrounded, since can't reach border
                    board[r][c] = "X"
        
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
