import os
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
        return random.choice(list(board.legal_moves))
