"""
hachess simulation expects the following methods:
- decide

"""

import os
import random
import chess


class Agent:
    def __init__(self) -> None:
        self.__init_agent_resources_path()

    def __init_agent_resources_path(self) -> None:
        """
        Initializes the path to the resources dir containing any static resources the agent might require.
        """
        self.__resources_path = os.path.join(
            os.path.split(os.path.abspath(__file__))[0], "resources"
        )

    def decide(self, board: chess.Board) -> chess.Move:
        pass
