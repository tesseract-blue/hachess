import chess, random

import numpy as np

from importlib import import_module

from hachess.agent import Agent

from typing import Union


class Simulation:
    def __init__(self, verbose: bool = False) -> None:
        """
        A simulation class that allows you to run two chess agents against each other.

        Args:
            verbose (bool, optional): Defaults to False.
        """
        self.__verbose = verbose
        self.__init_score()
        self.__init_agents()

    # INITIALIZATION

    def __init_logs(self, a1_name, a2_name) -> None:
        """

        "outcomes": list(),
                    "num_moves": list(),
                    "avg_move_times":

        SUMMARY

        Args:
            a1_name (_type_): _description_
            a2_name (_type_): _description_
        """
        self.__logs = {
            a1_name: {"score": 0, "summaries": list()},
            a2_name: {"score": 0, "summaries": list()},
            "games": list(),
        }

    def __init_score(self) -> None:
        "Initializes score dictionary"
        self.__score = dict()

    def __init_agents(
        self,
        a1: Agent = None,
        a2: Agent = None,
        a1_name: str = "a1",
        a2_name: str = "a2",
    ) -> None:
        "Initializes agents dictionary"
        self.__agents = {a1_name: a1, a2_name: a2}

    def __gen_gamelog(self, white, black) -> dict:
        return {
            white: {"color": "white", "outcome": None},
            black: {"color": "black", "outcome": None},
            "moves": {},
        }

    # PROPERTIES
    @property
    def agents(self):
        return self.__agents

    # PRIVATE METHODS
    def __choose_colors(self):
        rand = np.random.binomial(n=1, p=0.5)
        # white is index 0, black is index 1
        return rand, 1 - rand

    def __log_game(self, gamelog, white, black, outcome):
        outcome = [float(i) for i in outcome.split("-")]
        wo, bo = outcome[0], outcome[1]
        gamelog[white["outcome"]] += wo
        gamelog[black["outcome"]] += bo
        self.__logs["score"][white["name"]] += wo
        self.__logs["score"][black["name"]] += bo
        self.__logs

    def __run_game(
        self,
        white: dict[str, Union[str, Agent]],
        black: dict[str, Union[str, Agent]],
        move_time: int,
        game_time: int,
    ):
        wa, ba = white["agent"], black["agent"]
        gamelog = self.__gen_gamelog(white["name"], black["name"])

        board = chess.Board()

        while board.outcome() == None:
            if board.turn:  # white turn to move
                move = wa.decide(board)
            else:  # black turn to move
                move = ba.decide(board)
            try:
                board.push(move)  # push the selected move to the board object
            except (ValueError):
                if board.turn:
                    raise Exception(f"Invalid move by agent{white['name']}")
                else:
                    raise Exception(f"Inavlid move by agent {black['name']}")

        self.__log_game(gamelog, white, black, board.result())

    def __compete_agents(
        self,
        number_rounds: int,
        move_time: int,
        game_time: int,
    ) -> tuple[float, float]:
        self.__init_logs()
        for _ in range(number_rounds):
            colors = self.choose_colors()
            results = self.__run_game(
                self.agents[colors[0]], self.agents[colors[1]], move_time, game_time
            )

    # PUBLIC METHODS

    def run(
        self,
        a1: Agent,
        a2: Agent,
        games: int,
        move_time: int,
        game_time: int,
        a1_name: str = "a1",
        a2_name: str = "a2",
    ) -> None:
        """
        Runs the simulation, given the agent dir names.

        Args:
            A (str): _description_
            B (str): _description_
        """
        self.__init_agents(a1=a1, a2=a2, a1_name=a1_name, a2_name=a2_name)
        score = self.compete_agents(a1, a2, games, move_time, game_time)
        self.__logs["score"] = score
        return self.__logs


if __name__ == "__main__":
    sim = Simulation()
