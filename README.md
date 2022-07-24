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

## Other notes

- Each agent directory should contain a markdown file named `desc.md` which contains a minimum one sentence description of how the agent works.

# About

This repository is built to track on ongoing competition between [Hart](https://www.github.com/harttraveller) and [Adam](https://www.github.com/adamatbi) (hence the name: *H*art *A*dam _CHESS_).

# Rules

The nature of the competition is as follows: we create agents constructed in python/cython and pit them against each other. The only libraries we are allowed to use are numpy and python-chess.

Note that for the python-chess library, any module that takes any sort of _active role_ in making a decision in relation to a move is completely off limits. The purpose of this competition is to allow us to test our abilities to create agents that can make decisions, while only relying on base python (or cython, to accelerate game simulation), numpy (to help with linear algebra stuff that might be useful), and python-chess (mostly so we don't have to recreate a representation for the rules of chess, and can entirely focus on creating the game-playing algorithms).

For instance, you can write a Q-learning algorithm from scratch and train it, and then use the Q-table as a resource. You cannot, however, download a pre-trained Q-table. Likewise, you can explicitly program in, or create resources that encode/identify good moves (eg: forks, pins, etc), but you cannot download a pre-existing resources of forks, pins, and so on, and then use that. I have created `hart.py` and `adam.py` respectively to hold any common code that your agent might need to access, however, which can be found in the `common` dir. Essentially, your brain has to be a nexus which all chess related information passes through before being encoded in the agent.

Obviously, the stockfish SimpleEngine class in the python-chess library would completely off limits.

## Chess module, methods/properties agent is allowed to access

- chess.Board.legal_moves

## Chess module, methods/properties is NOT allowed to access

# Structure

There are three main directories at the root level of the repository, though only two of these will be visible on GitHub, as the third (`dev`) is included in the gitignore.

- games: contains a history of all games that have been run on the local machine
- dev: .gitignore'd - contains code Hart/Adam use to develop their algorithms
- hachess: contains all hachess module code

In the `hachess` directory there is: `hachess.py`, which contains the code such that agents can compete against one and other.

There are three other sub-directories in hachess. The first is `agents` - this directory contains all code relating to the agents.

The second is `resources` - this directory contains all files that may be required in order for an agent to run.

For example, suppose you create a Q-learning algorithm from scratch, which you then train yourself using the hachess library as an environment. You would want to include the Q-learning training code in the /dev directory, so it is opaque to the competitor. You would have to make the trained Q-table available to your agent, however, so you would put that in the /resources directory. Then, you would put your agent in the /agents directory.

Each agent should occupy a single python file, and the file should be named according to the following convention:

- [author name]\_[agent strategy].py

eg: hart_qlearnmixed.py

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

Note that several other libraries are included, however these are solely for enhanced library functionality, and are not for use in the agents themselves (not that they would help much anyways).'

## Agent Libraries

- [cython]()
- [numpy](https://github.com/numpy/numpy)
- [python-chess](https://github.com/niklasf/python-chess)

## hachess Libraries

- [rich](https://rich.readthedocs.io/en/stable/introduction.html)
- [plotly]
- [click]
- [markdown] (for writing chess game simulations to markdown/html reports?)
- ffmpeg-python? (for animating chess games)

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

## How to run a simulation

Just call `hach` from the command line. It will prompt you to select the agents you are using, and then it will begin to have them compete.

```bash
$ hach
$ Select Agent A >>>
$ Select Agent B >>>
```

When the agents have finished competing, a report will be generated in the `games` dir as a sub-directory. The sub-dir name is simply the datetime that you started the simulation at and the names of the agents competing with one and other.

## How to create a new agent

Creating a new agent is extremely simple. Simply copy the template directory in hachess.agents, and rename the template directory to whatever you want.

A template agent base class has already been provided for the agent. Here are a few quick notes:

- You should leave the class name as simply `Agent`.
- The `decide` method is required, and must return a type `chess.Move`
- The class initialization must not accept any parameters (besides `self`).

The Agent class is simple: it has one required method. This method is the `decide` method, which takes in a `chess.Board` type, and must return a `chess.Move` type. What the agent does to decide on a move is up to it. Note that if the agent takes longer than the pre-established `move_time` or `game_time`, the agent automatically loses. Furthermore, if the agent returns an illegal move, the agent also automatically loses. The loss reason is logged.

## Viewing a simulation report
