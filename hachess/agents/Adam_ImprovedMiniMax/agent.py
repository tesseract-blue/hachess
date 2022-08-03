"""
hachess simulation expects the following methods:
- decide
"""
import os
import time
import chess
from operator import itemgetter


class Agent:
    def __init__(self) -> None:
        self.__init_agent_resources_path()
        self.__init_memory()
        self.__num_evaluated = 0
        self.__depth = 3

    def __init_agent_resources_path(self) -> None:
        """
        Initializes the path to the resources dir containing any static resources the agent might require.
        """
        self.__resources_path = os.path.join(
            os.path.split(os.path.abspath(__file__))[0], "resources"
        )

    def __init_memory(self) -> None:
        """
        Initializes the game history, thus allowing the agent to inform its current strategy on the basis of previous games played.
        """
        self.__memory = list()

    def decide(self, board: chess.Board) -> chess.Move:
        self.__num_evaluated = 0
        return self.minimax(board, None, self.__depth, board.turn, True)[0]

    def minimax(
        self,
        board: chess.Board,
        move: chess.Move,
        depth: int,
        self_white: bool,
        self_move: bool,
    ) -> tuple[chess.Move, float]:
        """evaluates position using minimax tree search."""
        # evaluate if move is null once for efficency.
        if move != None:
            move_not_null = True
        else:
            move_not_null = False

        if move_not_null:
            # push move to board
            board.push(move)

        if depth == 0:
            # tree leaf reached. return evaluation of board position
            evaluation = (None, self.evaluate_position(board, self_white))
            if move_not_null:
                board.pop()
            return evaluation

        if board.outcome() != None:
            # check game is unresolved and return game result scores if resolved.
            result = (None, self.resolution_score(board.result(), self_white))
            if move_not_null:
                board.pop()
            return result

        branches = {
            (
                legal_move,
                self.minimax(board, legal_move, depth - 1, self_white, not self_move)[
                    1
                ],
            )
            for legal_move in board.legal_moves
        }

        if move_not_null:
            board.pop()

        if self_move:
            result = max(branches, key=itemgetter(1))
            return result
        else:
            result = min(branches, key=itemgetter(1))
            return result

    def evaluate_position(self, board: chess.Board, self_white: bool) -> float:
        """
        simple evaluation function using piece values. evaluates from side of player to move
        returns positive for agent advantage and negative for opponent advantage.

        """
        self.__num_evaluated += 1

        if board.outcome() != None:
            # check game is unresolved and return game result scores if resolved.
            return self.resolution_score(board.result(), self_white)

        black, white = board.occupied_co[0], board.occupied_co[1]
        pawns = board.pawns
        bishops = board.bishops
        knights = board.knights
        rooks = board.rooks
        queens = board.queens
        score = 100 * bin(pawns & white).count("1")
        score += 300 * bin(bishops & white).count("1")
        score += 300 * bin(knights & white).count("1")
        score += 500 * bin(rooks & white).count("1")
        score += 900 * bin(queens & white).count("1")
        score -= 100 * bin(pawns & black).count("1")
        score -= 300 * bin(bishops & black).count("1")
        score -= 300 * bin(knights & black).count("1")
        score -= 500 * bin(rooks & black).count("1")
        score -= 900 * bin(queens & black).count("1")

        return score if self_white else -score

    def resolution_score(self, board_result: str, self_white: bool) -> float:
        if board_result == "0-0":
            return 0
        elif board_result == "1-0":
            return 1000000 if self_white else -1000000
        else:
            return -1000000 if self_white else 1000000
