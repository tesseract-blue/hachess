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


def path_to_agents() -> str:
    "Returns the path to the agents dir"
    return os.path.join(os.path.split(os.path.abspath(__file__))[0], "agents")


def sinput(options: list[str]) -> Any:
    """
    TODO: fill in later

    Args:
        prompt (str, optional): _description_. Defaults to "".

    Kwargs:
        type (type, optional):
        options (list, optional):

    Returns:
        Any: _description_
    """
    user_input = input(f">>> ")
    while user_input not in options:
        vprint("[bold red]INVALID PARAMETER[/bold red]", verbose=True)
        user_input = str(input(f">>> "))
    return user_input


def select_agent(ctx, agent_id: str, verbose: bool) -> str:
    available_agents = os.listdir(path_to_agents())

    # prompt the user to select agent (based on list item number)
    vprint(
        f"[blue]Please select agent {agent_id} from the list:[/blue]",
        verbose=ctx.obj["VERBOSE"],
    )

    # display agents
    for i, v in enumerate(available_agents):
        print(f"{i}: {v}")

    # return user selected agent
    agent_index = sinput(options=[str(i) for i in range(len(available_agents))])
    return available_agents[int(agent_index)]
