"""
Connect4 - combines notebook logic + streamlit interface
"""

import numpy as np
from typing import Optional, List


class Connect4:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.last_move = None
        self.current_player = 1  # For streamlit
        
    def reset(self):
        """Reset game"""
        self.board = np.zeros((self.rows, self.cols), dtype=int)
        self.last_move = None
        self.current_player = 1
        
    def is_valid_move(self, col: int) -> bool:
        """Check if column has space (for streamlit)"""
        if col < 0 or col >= self.cols:
            return False
        return self.board[0][col] == 0
    
    def get_valid_moves(self):
        """Get valid moves from center out (for notebook agent)"""
        center = self.cols // 2
        moves = []
        for i in range(self.cols):
            col = center + (1 - 2 * (i % 2)) * (i + 1) // 2
            if self.board[0][col] == 0:
                moves.append(col)
        return moves

    def make_move(self, col, player=None):
        """Make move - works for both streamlit and notebook"""
        if player is None:
            player = self.current_player
        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = player
                self.last_move = (r, col)
                return r
        return None

    def undo_move(self, col, row):
        """Undo move (for notebook agent)"""
        self.board[row][col] = 0
        self.last_move = None

    def is_win_at(self, row, col, player):
        """Check if position is winning"""
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for delta in [1, -1]:
                r, c = row + delta * dr, col + delta * dc
                while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == player:
                    count += 1
                    r += delta * dr
                    c += delta * dc
            if count >= 4:
                return True
        return False

    def is_terminal(self):
        """Check if game ended (for notebook agent)"""
        if self.last_move:
            r, c = self.last_move
            if self.is_win_at(r, c, self.board[r][c]):
                return self.board[r][c]
        if not np.any(self.board[0] == 0):
            return 0
        return None
    
    def check_winner(self) -> Optional[int]:
        """Check winner (for streamlit)"""
        if self.last_move:
            r, c = self.last_move
            if self.is_win_at(r, c, self.board[r][c]):
                return self.board[r][c]
        if not self.get_valid_moves():
            return 0
        return None
    
    def switch_player(self):
        """Switch player (for streamlit)"""
        self.current_player = 2 if self.current_player == 1 else 1
    
    def get_board_copy(self) -> np.ndarray:
        """Get board copy"""
        return self.board.copy()
