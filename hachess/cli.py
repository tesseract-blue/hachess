# standard libary
import os

# single libraries
import click

# external module
from typing import Any

# package library
from hachess.common import vprint, select_agent
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


if __name__ == "__main__":
    cli()
