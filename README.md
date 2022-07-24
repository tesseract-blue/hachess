<div align="center" id="top">
  <img src="https://media4.giphy.com/media/Spty0N8Cg3lNMnFLoB/giphy.gif" width="240" alt="hachess"/>
</div>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#install">Install</a> &#xa0; | &#xa0;
  <a href="#tutorial">Tutorial</a> &#xa0; | &#xa0;
  <a href="#agents">Agents</a> &#xa0; | &#xa0;
  <a href="#rules">Rules</a>

</p>

# About

This repository is built to track on ongoing competition between [Hart](https://www.github.com/harttraveller) and [Adam](https://www.github.com/adamatbi) (hence the name: *H*art *A*dam _CHESS_).

The nature of the competition is as follows: we create agents constructed in python/cython and pit them against each other. The only libraries we are allowed to use are:

- [numpy](https://github.com/numpy/numpy)
- [python-chess](https://github.com/niklasf/python-chess)

Note that for the python-chess library, any module that takes any sort of _active role_ in making a decision in relation to a move is completely off limits.

# Requirements

- Base python
- Cython

# Install

```bash
$ pip install git+https://
```

# Rules

We can only use the listed libraries. As a general rule of thumb, anything that is prebuilt (something someone else built related to move selection for chess) to choose moves for us is not allowed.

## Allowed

You can write a Q-learning algorithm from scratch and train it, and then use the Q-table as a resource.

## Not Allowed

The stockfish SimpleEngine class in the python-chess library.

## Libraries

**For the agents, only the following libraries are allowed**

- python-chess
- numpy
