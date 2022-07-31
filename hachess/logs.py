from dataclasses import dataclass
import numpy as np

from hachess.analyze import (
    color_distribution,
    score_distribution,
    color_score_distribution,
)
import pandas as pd


class SingleGame:
    """Class for keeping track of an item in inventory."""

    def __init__(self, a1_name: str, a2_name: str, a1_color: str, a2_color: str):

        # agent names
        self.a1_name = f"[A1] {a1_name}"
        self.a2_name = f"[A2] {a2_name}"

        # agent colors
        self.a1_color = a1_color
        self.a2_color = a2_color

        # game complete
        self.complete: bool = False

        # move logs
        self.moves: list[str] = list()

        # outcome
        self.a1_score: float = None
        self.a2_score: float = None
        self.reason: str = None  # reason for win/lose (checkmate, on time (per move, or overall), invalid move, etc)

        # invididual move times
        self.a1_times: list[float] = list()
        self.a2_times: list[float] = list()

        # total move time
        self.a1_total_time: float = None
        self.a2_total_time: float = None

        # mean move time
        self.a1_mean_time: float = None
        self.a2_mean_time: float = None

        # move time standard deviation
        self.a1_stdev_time: float = None
        self.a2_stdev_time: float = None

    # CALCULATIONS

    def __compute_time_stats(self) -> None:
        assert self.complete, "Time stats cannot be computed until the game is complete"
        # self.a1_total_time = sum(self.a1_times)
        # self.a2_total_time = sum(self.a2_times)
        # self.a1_mean_time = self.a1_total_time / len(self.a1_times)
        # self.a2_mean_time = self.a2_mean_time / len(self.a2_times)
        # self.a1_stdev_time = np.array(self.a1_times).std()
        # self.a2_stdev_time = np.array(self.a2_times).std()

    # SETTERS

    ## Private Setters

    def __log_outcome(self, a1_score: float, a2_score: float, reason: str) -> None:
        self.a1_score = a1_score
        self.a2_score = a2_score
        self.reason = reason
        self.complete = True

    ## Public Setters

    def set_colors(self, a1_color: str, a2_color: str) -> None:
        assert {a1_color, a2_color} == {"W", "B"}, "Invalid agent colors"
        self.a1_color = a1_color
        self.a2_color = a2_color

    def log_move(self, move: str) -> None:
        self.moves.append(move)

    def log_times(self, a1_time: float = None, a2_time: float = None) -> None:
        if a1_time is not None:
            self.a1_times.append(a1_time)
        if a2_time is not None:
            self.a2_times.append(a2_time)

    def log_outcome(self, a1_score: float, a2_score: float, reason: str) -> None:
        if {a1_score, a2_score} == {0.5}:
            assert reason in {
                "stalemate",
                "limited material + time (move)",
                "limited material + time (game)",
                "dev",
            }, f"Invalid reason: `{reason}`"
            self.__log_outcome(a1_score=a1_score, a2_score=a2_score, reason=reason)
        elif {a1_score, a2_score} == {1, 0}:
            assert reason in (
                "checkmate",
                "invalid move",
                "time (move)",
                "time (game)",
                "dev",
            ), f"Invalid reason: `{reason}`"
            self.__log_outcome(a1_score=a1_score, a2_score=a2_score, reason=reason)
        else:
            raise Exception("Impossible outcome score for game")

    # GETTERS
    @property
    def logs(self) -> dict:
        self.__compute_time_stats()
        return {
            "a1_name": self.a1_name,
            "a2_name": self.a2_name,
            "a1_color": self.a1_color,
            "a2_color": self.a2_color,
            "a1_score": self.a1_score,
            "a2_score": self.a2_score,
            "a1_times": self.a1_times,
            "a2_times": self.a2_times,
            "a1_total_time": self.a1_total_time,
            "a2_total_time": self.a2_total_time,
            "a1_mean_time": self.a1_mean_time,
            "a2_mean_time": self.a2_mean_time,
            "a1_stdev_time": self.a1_stdev_time,
            "a2_stdev_time": self.a2_stdev_time,
            "moves": self.moves,
            "num_moves": len(self.moves),
            "reason": self.reason,
        }


@dataclass
class MultipleGames:
    """
    Class for keeping track of multiple games
    """

    a1_name: str
    a2_name: str

    num_rounds: int

    def __post_init__(self):
        self.finished: bool = False
        self.stats: dict = dict()
        self.games: list[dict] = list()

    def compute_game_statistics(self, logs: pd.DataFrame):
        game_stats = dict()
        # color distribution
        game_stats["color_distribution"] = color_distribution(logs)
        # score distribution
        game_stats["score_distribution"] = score_distribution(logs)
        # # score distribution by color
        # self.csdist = color_score_distribution(logs)
        # TODO: reason distribution
        # TODO: reason distribution by agent
        # time stats
        # mean: total time per game
        # mean: mean move time per game
        # mean: standard dev of move time per game
        # moves per game

    def log_game(self, game: dict) -> None:
        self.games.append(game.logs)

    @property
    def logs(self):
        df = pd.DataFrame(self.games).drop(["a1_times", "a2_times", "moves"], axis=1)
        self.compute_game_statistics(df)
        return self.cdist, self.sdist
