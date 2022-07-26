# standard libary
import os

# single libraries
import click

# external module
from typing import Any

# package library
from hachess.common import vprint
from hachess.simulate import Simulation


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


@click.group()
@click.option("--debug", default=True)
@click.option("--verbose", default=True)
@click.pass_context
def cli(ctx, debug, verbose):
    print()
    vprint(
        f"Debug mode is {'[green]on[/green]' if debug else '[red]off[/red]'}",
        verbose=verbose,
    )
    vprint(
        f"Verbose mode is {'[green]on[/green]' if verbose else '[red]off[/red]'}",
        verbose=verbose,
    )
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    ctx.obj["VERBOSE"] = verbose
    print()


@cli.command()
@click.option(
    "--move_time",
    default=-1,
    type=int,
    help="The amount of time (seconds) each agent has to move per turn. Default: -1 (infinite time)",
)
@click.option(
    "--game_time",
    default=-1,
    type=int,
    help="The amount of time (seconds) each agent has to move over the game. Default: -1 (infinite time)",
)
@click.option(
    "--games",
    default=100,
    type=int,
    help="The number of games the agents should play to move over the game. Default: 100",
)
@click.pass_context
def run(ctx, move_time: int, game_time: int, games: int) -> None:
    """
    CLI command to run two agents against each other.

    Args:
        ctx (_type_): _description_
        move_time (int): _description_
        game_time (int): _description_
    """
    vprint("[bold green]SIMULATION STARTING[/bold green]", verbose=ctx.obj["VERBOSE"])

    # prompt user for the first agent
    A = select_agent(ctx, "A", verbose=ctx.obj["VERBOSE"])

    # prompt user for the second agent
    B = select_agent(ctx, "B", verbose=ctx.obj["VERBOSE"])

    # actually run the simulation, gather logs
    sim = Simulation(verbose=ctx.obj["VERBOSE"])
    logs = sim.run(A, B, games, move_time, game_time)
    print(logs)

    ## check to see if there is a logs directory in the module directory, if there isn't, create one

    # output logs to the predefined logs directory


@cli.command()
@click.pass_context
def analyze(ctx):
    vprint("[bold green]Analysis[/bold green]", verbose=ctx.obj["VERBOSE"])
