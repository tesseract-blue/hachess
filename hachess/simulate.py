import chess, random

from typing import Union

from hachess.agent import Agent
from hachess.logs import SingleGame, MultipleGames
import numpy as np

from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    SpinnerColumn,
    MofNCompleteColumn,
)


class Simulation:
    def __init__(self, verbose: bool = False) -> None:
        """
        A simulation class that allows you to run two chess agents against each other.

        Args:
            verbose (bool, optional): Defaults to False.
        """
        self.__verbose = verbose

    # PRIVATE METHODS

    def __run_game(
        self,
        a1: dict[str, Union[str, Agent]],
        a2: dict[str, Union[str, Agent]],
        move_time: int,
        game_time: int,
    ):
        color = np.random.binomial(1, 0.5)  # if this returns zero, a1 is white
        a1_color = "B" if color else "W"
        a2_color = "W" if color else "B"
        gamelog = SingleGame(
            a1["name"],
            a2["name"],
            a1_color,
            a2_color,
        )

        board = chess.Board()

        while board.outcome() == None:
            if color - board.turn:  # if color == 0, then white moves first
                move = a1["agent"].decide(board)
            else:
                move = a2["agent"].decide(board)
            try:
                board.push(move)  # push the selected move to the board object
            except ValueError:
                raise Exception(f"Invalid move generated")

        outcome = [float(i) for i in board.result().replace("1/2", "0.5").split("-")]
        a1_score = outcome[0] if a1_color == "W" else outcome[1]
        a2_score = outcome[0] if a2_color == "W" else outcome[1]
        gamelog.log_outcome(a1_score, a2_score, "dev")
        return gamelog

    # PUBLIC METHODS

    def run(
        self,
        a1: dict[str, Union[str, Agent]],
        a2: dict[str, Union[str, Agent]],
        num_rounds: int,
        move_time: int,
        game_time: int,
    ) -> None:
        """
        Runs the simulation, given the agent dir names.
        """
        self.__logs = MultipleGames(a1["name"], a2["name"], num_rounds)

        progress = Progress(
            SpinnerColumn(),
            BarColumn(),
            MofNCompleteColumn(),
            TimeRemainingColumn(),
        )
        with progress:
            task = progress.add_task("running simulation", total=num_rounds)
            for _ in range(num_rounds):
                gamelog = self.__run_game(a1, a2, move_time, game_time)
                self.__logs.log_game(gamelog)
                progress.advance(task)
        return self.__logs.logs


if __name__ == "__main__":
    sim = Simulation()
