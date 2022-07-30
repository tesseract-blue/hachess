import os

from typing import Any
from pprint import pprint

from rich.console import Console


def vprint(
    s: Any,
    verbose: bool,
    pretty: bool = False,
    sort_dicts: bool = False,
    limit: int = None,
) -> None:
    if limit is not None:
        p = s[:limit]
    else:
        p = s
    if verbose:
        if pretty:
            pprint(p)
        else:
            Console().print(p)


def hachess_local_directory() -> str:
    return os.path.split(os.path.abspath(__file__))[0]


def identify_agent_class(path: str) -> str:
    """
    Identifies names of the agent class in path to agent directory

    Args:
        path (str): path to agent dir

    Returns:
        str: the name of the agent class
    """
    if os.path.exists(path):
        files = [f.split(".") for f in os.listdir(path) if len(f.split(".")) == 2]
        pyfile = [i for i in files if (i[1] == "py") and (i[0] != "__init__")]
        if len(pyfile) == 1:
            pyfile = ".".join(pyfile[0])
            with open(f"{path}/{pyfile}") as pf:
                classname = pf.read().split("class ")[1].split(":")[0]
                return classname
        elif len(pyfile) == 2:
            raise Exception(
                "There is more than one python file in the agent directory."
            )
        else:
            raise Exception("There are no python files in the agent directory.")

    else:
        raise Exception("The path does not exist.")
