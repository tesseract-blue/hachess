<div align="center" id="top">
  <img src="https://media4.giphy.com/media/Spty0N8Cg3lNMnFLoB/giphy.gif" width="240" alt="hachess"/>
</div>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0;
  <a href="#rules">Rules</a> &#xa0; | &#xa0;
  <a href="#structure">Structure</a> &#xa0; | &#xa0;
  <a href="#time">Time</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#install">Install</a> &#xa0; | &#xa0;
  <a href="#agents">Agents</a> &#xa0; | &#xa0;
  <a href="#rules">Rules</a>

</p>

# About

This repository is built to track on ongoing competition between [Hart](https://www.github.com/harttraveller) and [Adam](https://www.github.com/adamatbi) (hence the name: *H*art *A*dam _CHESS_).

# Rules

The nature of the competition is as follows: we create agents constructed in python/cython and pit them against each other. The only libraries we are allowed to use are numpy and python-chess.

Note that for the python-chess library, any module that takes any sort of _active role_ in making a decision in relation to a move is completely off limits. The purpose of this competition is to allow us to test our abilities to create agents that can make decisions, while only relying on base python (or cython, to accelerate game simulation), numpy (to help with linear algebra stuff that might be useful), and python-chess (mostly so we don't have to recreate a representation for the rules of chess, and can entirely focus on creating the game-playing algorithms).

For instance, you can write a Q-learning algorithm from scratch and train it, and then use the Q-table as a resource. You cannot, however, download a pre-trained Q-table. Likewise, you can explicitly program in, or create resources that encode/identify good moves (eg: forks, pins, etc), but you cannot download a pre-existing resources of forks, pins, and so on, and then use that. Essentially, your brain has to be a nexus which all chess related information passes through before being encoded in the agent.

Obviously, the stockfish SimpleEngine class in the python-chess library would completely off limits.

# Structure

In the `hachess` directory there is: `hachess.py`, which contains the code such that agents can compete against one and other.

There are three other sub-directories in hachess. The first is `agents` - this directory contains all code relating to the agents.

The second is `resources` - this directory contains all files that may be required in order for an agent to run.

# Time

When running two algorithms against each other it is necessary to constrain the amount of time each algorithm takes to make a decision. Accordingly, there are two parameters provided to the simulation engine:

- move_time: the amount of time an agent can take per move
- game_time: the amount of time an agent can take per game

If an agent takes longer than `move_time` in a given move, or takes longer than `game_time` over the course of a given game, the agent loses.

A good target for testing agents is as follows:

We should be able to leave two agents competing when we go to bed, and expect that they will have played 100 games by the time we wake up.

This equates to around 100 games in 6 hours, or one game every 36 seconds.

Good parameters might then be:

- move_time: 1
- game_time: 36 (each agent receives 18 seconds)

# Requirements

- [numpy](https://github.com/numpy/numpy)
- [python-chess](https://github.com/niklasf/python-chess)
- [click](https://click.palletsprojects.com/en/8.1.x/)
- [rich](https://rich.readthedocs.io/en/stable/introduction.html)

# Install

Before starting, make sure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed. If you plan on creating agents please use the second installation method.

## Installation (Basic)

```bash
$ pip install git+https://github.com/harttraveller/hachess.git
```

## Installation (Agent Development)

First clone the repository to a place you would like to work on it.

```bash
$ git clone git+https://github.com/harttraveller/hachess.git
```

Next, enter the repository directory and run the following command.

```bash
$ conda env create -f environment.yml
```

Finally, while in the root directory you cloned, with the hachess environment activated, run the following command.

```bash
$ pip install -e .
```

# Tutorial

# Documentation
