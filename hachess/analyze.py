"""

TODO
- add a graph that shows all per move game times on graph, superimposed.
    - would expect a downwards trend for many algorithms.

"""
import pandas as pd


def color_distribution(logs: pd.DataFrame) -> dict:
    cdist = dict()
    cdist["a1_color"] = logs["a1_color"].value_counts().to_dict()
    cdist["a2_color"] = logs["a2_color"].value_counts().to_dict()
    return cdist


def score_distribution(logs: list[dict]) -> dict:
    sdist = dict()
    sdist["a1_score"] = logs["a1_score"].sum()
    sdist["a2_score"] = logs["a2_score"].sum()
    return sdist


def color_score_distribution(logs: list[dict]) -> dict:
    csdist = {logs.a1_name: {"W": 0, "B": 0}, logs.a2_name: {"W": 0, "B": 0}}
    for game in logs.games:
        csdist[logs.a1_name][game[logs.a1_name]["color"]] += [
            game[logs.a1_name]["score"]
        ]
        csdist[logs.a2_name][game[logs.a2_name]["color"]] += [
            game[logs.a1_name]["score"]
        ]
    return csdist


def total_reason_distribution(logs: list[dict]) -> dict:
    pass


def agent_reason_distribution(logs: list[dict]) -> dict:
    pass


def moves_per_game(logs: list[dict]) -> list:
    return [i["num_moves"] for i in logs.games]
