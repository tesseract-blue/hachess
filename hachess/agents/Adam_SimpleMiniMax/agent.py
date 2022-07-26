"""
hachess simulation expects the following methods:
- decide


The agent randomly selects a move from the list of legal moves.

"""
import os
from copy import deepcopy
import random
import chess


class Agent:
    def __init__(self) -> None:
        self.__init_agent_resources_path()
        self.__init_memory()

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
        return self.minimax(board, 2, True)

    def minimax(self, board: chess.Board, depth: int, self_move: bool) -> chess.Move:
        """evaluates position using minimax tree search."""
        for i in list(board.legal_moves):
            if self_move:
                # agent has move
                if depth == 0:
                    # return choice based on evaluation function
                    pass

        return list(board.legal_moves)[0]

    def evaluate_position(self, board: chess.Board, self_move: bool) -> float:
        return 0.0
