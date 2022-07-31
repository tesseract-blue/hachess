# standard libary
import os

# single libraries
import click

# external module
from typing import Any

# package library
from hachess.common import vprint, select_agent, import_path_agent
from hachess.simulate import Simulation


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
    "--a1",
    default="default",
    type=str,
    help="The path to the directory containing the first agent you want to use",
    required=False,
)
@click.option(
    "--a2",
    default="default",
    type=str,
    help="The path to the directory containing the second agent you want to use",
    required=False,
)
@click.option(
    "--logs",
    default="default",
    type=str,
    help="The path to the directory you want the games logs to save to",
    required=False,
)
@click.option(
    "--move_time",
    default=-1,
    type=int,
    help="The amount of time (seconds) each agent has to move per turn. Default: -1 (infinite time)",
    required=False,
)
@click.option(
    "--game_time",
    default=-1,
    type=int,
    help="The amount of time (seconds) each agent has to move over the game. Default: -1 (infinite time)",
    required=False,
)
@click.option(
    "--num_rounds",
    default=100,
    type=int,
    help="The number of rounds the agents should play. Default: 100",
    required=False,
)
@click.pass_context
def run(
    ctx, a1: str, a2: str, logs: str, move_time: int, game_time: int, num_rounds: int
) -> None:
    """
    CLI command to run two agents against each other.

    Args:
        ctx (_type_): _description_
        a1 (str):
        a2 (str):
        logs (str):
        move_time (int): _description_
        game_time (int): _description_
    """
    vprint("[bold green]RUNNING HACHESS[/bold green]", verbose=ctx.obj["VERBOSE"])

    if (a1 == "default") and (a2 == "default"):
        # prompt user for agent selection
        a1 = select_agent(ctx, "a1", verbose=ctx.obj["VERBOSE"])
        a2 = select_agent(ctx, "a2", verbose=ctx.obj["VERBOSE"])
    elif (a1 != "default") and (a2 != "default"):
        a1 = import_path_agent(ctx, a1, verbose=ctx.obj["VERBOSE"])
        a2 = import_path_agent(ctx, a2, verbose=ctx.obj["VERBOSE"])
    else:
        raise Exception("You cannot pass only a single agent path.")

    sim = Simulation(verbose=ctx.obj["VERBOSE"])
    logs = sim.run(a1, a2, num_rounds, move_time, game_time)
    vprint(logs, verbose=True)

    ## check to see if there is a logs directory in the module directory, if there isn't, create one

    # output logs to the predefined logs directory


@cli.command()
@click.pass_context
def analyze(ctx):
    vprint("[bold green]Analysis[/bold green]", verbose=ctx.obj["VERBOSE"])


if __name__ == "__main__":
    cli()
