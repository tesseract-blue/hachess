<div align="center" id="top">
  <img src="https://media4.giphy.com/media/Spty0N8Cg3lNMnFLoB/giphy.gif" width="128" alt="hachess"/>
</div>

<br>

<div align="center">
  <a href="https://github.com/tesseract-blue/hachess" rel="nofollow">
    <img src="https://img.shields.io/github/stars/tesseract-blue/hachess" alt="Stars">
  </a>
  <!-- <a href="https://github.com/tesseract-blue/hachess">
    <img src="https://github.com/tesseract-blue/hachess/workflows/Tests/badge.svg?event=push&branch=main" />
  </a> -->
  <a href="https://github.com/tesseract-blue/hachess/blob/main/LICENSE">
    <img alt="license" src="https://img.shields.io/badge/license-MIT-blue" />
  </a>
  <a href="https://discord.gg/ua4BJjNt">
    <img alt="discord" src="https://img.shields.io/discord/1001555468679913574?color=5865F2&label=discord&logo=discord&logoColor=8a9095">
  </a>
  <br/>
  <br/>
  <a href="#about">About</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="#install">Install</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="#quickstart">Quickstart</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="#documentation">Documentation</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="#features">Features</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="#tasks">Tasks</a>
  <br />

</div>

<br>

# About

This library allows you to pit chess playing agents against each other in a simulated environment, and monitor their progress as they play.

At its core, the purpose of `hachess` is to facilitate competitive meta-chess. Instead of just playing chess, you can write algorithms to play chess, and compete with friends to see who can write the best algorithm.

You can and probably should set restrictions on what can and can't be used if you use this library for competitive purposes. The authors of the library have an ongoing competition. The rules of their competition can be found in the [COMPETITION](COMPETITION.md) file.

# Install

## _Requirements_

- [python-chess](https://github.com/niklasf/python-chess)
- [cython]()
- [numba]()
- [numpy](https://github.com/numpy/numpy)
- [rich](https://rich.readthedocs.io/en/stable/introduction.html)
- [plotly]()
- [click]()
- [flask]()

## _Instructions_

It is recommended you use [conda](https://docs.conda.io/en/latest/miniconda.html) for environment management. You can create a new environment with:

```
$ conda create --name hachess python=3.10
```

Then, you can install the package with:

```bash
$ pip install git+https://github.com/harttraveller/hachess.git
```

We intend to configure the package with PyPi soon.

# Quickstart

## _CLI: Running a simulation_

You can run a simulation with the prepackaged agents, or run a simulation with your own agent class.

**Example Agents**

Just call `hach` from the command line. It will prompt you to select the agents you are using, and then it will begin to have them compete.

```bash
$ hach
$ Select Agent A >>>
$ Select Agent B >>>
```

When the agents have finished competing, a report will be generated in the `games` dir as a sub-directory. The sub-dir name is simply the datetime that you started the simulation at and the names of the agents competing with one and other.

**Your Agents**

## _Python: Running a simulation_

## _Creating a new agent_

Creating a new agent is extremely simple. Simply copy the template directory in hachess.agents, and rename the template directory to whatever you want.

A template agent base class has already been provided for the agent. Here are a few quick notes:

- You should leave the class name as simply `Agent`.
- The `decide` method is required, and must return a type `chess.Move`
- The class initialization must not accept any parameters (besides `self`).

The Agent class is simple: it has one required method. This method is the `decide` method, which takes in a `chess.Board` type, and must return a `chess.Move` type. What the agent does to decide on a move is up to it. Note that if the agent takes longer than the pre-established `move_time` or `game_time`, the agent automatically loses. Furthermore, if the agent returns an illegal move, the agent also automatically loses. The loss reason is logged.

## _Viewing a simulation report_

asdf

# Documentation

The library we are using for managing chess games is [python-chess](https://github.com/niklasf/python-chess). You can also reference their documentation.

# Features

## _Implemented_

## _Todo_

- Add a rich dashboard to monitor games as they are taking place.

# Tasks

- List package on pypi
