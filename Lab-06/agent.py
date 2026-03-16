"""
Agents from ConnectFour.ipynb
"""

import numpy as np
from typing import List
import random
import math


class Agent:
    """Base class for Streamlit interface"""
    def get_move(self, board: np.ndarray, valid_moves: List[int]) -> int:
        raise NotImplementedError()


class RandomAgent(Agent):
    """Random agent"""
    def get_move(self, board: np.ndarray, valid_moves: List[int]) -> int:
        return random.choice(valid_moves)


class MinimaxAgent:
    """MinimaxAgent from notebook"""
    def __init__(self, player_id, depth=4):
        self.player_id = player_id
        self.opp_id = 1 if player_id == 2 else 2
        self.depth = depth
        self.nodes_visited = 0

    def evaluate(self, game):
        # Normalización de estados terminales
        res = game.is_terminal()
        if res == self.player_id: return 100000
        if res == self.opp_id: return -100000
        if res == 0: return 0

        score = 0
        
        # Control del centro: bono estático por dominio de la columna central
        center_col = game.cols // 2
        center_array = [int(i) for i in list(game.board[:, center_col])]
        score += center_array.count(self.player_id) * 6

        # Recorrido por Sliding Window para evaluar sub-arreglos de 4 casillas
        def evaluate_window(window, player, opponent):
            win_score = 0
            
            # Premiar amenazas propias detectando rutas bloqueadas (count(0) == 1)
            if window.count(player) == 3 and window.count(0) == 1:
                win_score += 50  
            elif window.count(player) == 2 and window.count(0) == 2:
                win_score += 10
                
            # Prioridad defensiva: castigo asimétrico para forzar bloqueos
            if window.count(opponent) == 3 and window.count(0) == 1:
                win_score -= 80  
            elif window.count(opponent) == 2 and window.count(0) == 2:
                win_score -= 15
                
            return win_score

        # Barrido horizontal
        for r in range(game.rows):
            row_array = [int(i) for i in list(game.board[r,:])]
            for c in range(game.cols - 3):
                window = row_array[c:c+4]
                score += evaluate_window(window, self.player_id, self.opp_id)

        # Barrido vertical
        for c in range(game.cols):
            col_array = [int(i) for i in list(game.board[:,c])]
            for r in range(game.rows - 3):
                window = col_array[r:r+4]
                score += evaluate_window(window, self.player_id, self.opp_id)

        # Barrido de diagonales
        for r in range(game.rows - 3):
            for c in range(game.cols - 3):
                # Pendiente positiva
                window = [game.board[r+i][c+i] for i in range(4)]
                score += evaluate_window(window, self.player_id, self.opp_id)
                
                # Pendiente negativa
                window = [game.board[r+3-i][c+i] for i in range(4)]
                score += evaluate_window(window, self.player_id, self.opp_id)

        return score

    def get_best_move(self, game):
        self.nodes_visited = 0
        best_val = -math.inf
        moves = game.get_valid_moves()
        best_move = moves[0] if moves else None
        
        for col in moves:
            row = game.make_move(col, self.player_id)
            val = self._minimax(game, self.depth - 1, False)
            game.undo_move(col, row)
            if val > best_val:
                best_val, best_move = val, col
        return best_move

    def _minimax(self, game, depth, is_maximizing):
        self.nodes_visited += 1
        term = game.is_terminal()
        
        if depth == 0 or term is not None:
            return self.evaluate(game)

        if is_maximizing:
            val = -math.inf
            for col in game.get_valid_moves():
                row = game.make_move(col, self.player_id)
                val = max(val, self._minimax(game, depth - 1, False))
                game.undo_move(col, row)
            return val
        else:
            val = math.inf
            for col in game.get_valid_moves():
                row = game.make_move(col, self.opp_id)
                val = min(val, self._minimax(game, depth - 1, True))
                game.undo_move(col, row)
            return val


class AlphaBetaAgent(MinimaxAgent):
    """AlphaBetaAgent from notebook"""
    def get_best_move(self, game):
        self.nodes_visited = 0
        best_val, alpha, beta = -math.inf, -math.inf, math.inf
        moves = game.get_valid_moves()
        best_move = moves[0] if moves else None

        for col in moves:
            row = game.make_move(col, self.player_id)
            val = self._alpha_beta(game, self.depth - 1, alpha, beta, False)
            game.undo_move(col, row)
            
            if val > best_val:
                best_val, best_move = val, col
            
            alpha = max(alpha, best_val)
        return best_move

    def _alpha_beta(self, game, depth, alpha, beta, is_maximizing):
        self.nodes_visited += 1
        term = game.is_terminal()
        
        if depth == 0 or term is not None:
            return self.evaluate(game)

        if is_maximizing:
            val = -math.inf
            for col in game.get_valid_moves():
                row = game.make_move(col, self.player_id)
                val = max(val, self._alpha_beta(game, depth - 1, alpha, beta, False))
                game.undo_move(col, row)
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return val
        else:
            val = math.inf
            for col in game.get_valid_moves():
                row = game.make_move(col, self.opp_id)
                val = min(val, self._alpha_beta(game, depth - 1, alpha, beta, True))
                game.undo_move(col, row)
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return val


class NotebookConnect4:
    """Connect4 from notebook - needed for agent"""
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.last_move = None

    def get_valid_moves(self):
        center = self.cols // 2
        moves = []
        for i in range(self.cols):
            col = center + (1 - 2 * (i % 2)) * (i + 1) // 2
            if self.board[0][col] == 0:
                moves.append(col)
        return moves

    def make_move(self, col, player):
        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = player
                self.last_move = (r, col)
                return r
        return None

    def undo_move(self, col, row):
        self.board[row][col] = 0
        self.last_move = None

    def is_win_at(self, row, col, player):
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
        if self.last_move:
            r, c = self.last_move
            if self.is_win_at(r, c, self.board[r][c]):
                return self.board[r][c]
        if not np.any(self.board[0] == 0):
            return 0
        return None


class MyAgent(Agent):
    """Streamlit adapter for AlphaBetaAgent"""
    def __init__(self):
        self.agent = AlphaBetaAgent(player_id=2, depth=6)
    
    def get_move(self, board: np.ndarray, valid_moves: List[int]) -> int:
        game = NotebookConnect4()
        game.board = board.copy()
        return self.agent.get_best_move(game)