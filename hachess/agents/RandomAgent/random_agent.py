import random
import chess


class RandomAgent:
    def decide(self, board: chess.Board) -> chess.Move:
        return random.choice(list(board.legal_moves))
