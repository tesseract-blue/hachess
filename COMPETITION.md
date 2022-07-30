# Introduction

This repository is built to track on ongoing competition between [Hart](https://www.github.com/harttraveller) and [Adam](https://www.github.com/adamatbi) (hence the name: *H*art *A*dam _CHESS_).

# Rules

The nature of the competition is as follows: we create agents constructed in python/cython and pit them against each other. The only libraries we are allowed to use are numpy and python-chess.

Note that for the python-chess library, any module that takes any sort of _active role_ in making a decision in relation to a move is completely off limits. The purpose of this competition is to allow us to test our abilities to create agents that can make decisions, while only relying on base python (or cython, to accelerate game simulation), numpy (to help with linear algebra stuff that might be useful), and python-chess (mostly so we don't have to recreate a representation for the rules of chess, and can entirely focus on creating the game-playing algorithms).

For instance, you can write a Q-learning algorithm from scratch and train it, and then use the Q-table as a resource. You cannot, however, download a pre-trained Q-table. Likewise, you can explicitly program in, or create resources that encode/identify good moves (eg: forks, pins, etc), but you cannot download a pre-existing resources of forks, pins, and so on, and then use that. I have created `hart.py` and `adam.py` respectively to hold any common code that your agent might need to access, however, which can be found in the `common` dir. Essentially, your brain has to be a nexus which all chess related information passes through before being encoded in the agent.

Obviously, the stockfish SimpleEngine class in the python-chess library would completely off limits.

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
