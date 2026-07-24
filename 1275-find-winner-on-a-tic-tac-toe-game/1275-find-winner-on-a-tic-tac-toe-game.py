class Solution:
    def tictactoe(self, moves):
        grid = [['']*3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            grid[r][c] = 'A' if i % 2 == 0 else 'B'
        
        lines = [grid[i] for i in range(3)] + \
                [[grid[i][j] for i in range(3)] for j in range(3)] + \
                [[grid[i][i] for i in range(3)], [grid[i][2-i] for i in range(3)]]
        
        for line in lines:
            if line[0] == line[1] == line[2] and line[0]:
                return line[0]
        
        return "Pending" if len(moves) < 9 else "Draw"