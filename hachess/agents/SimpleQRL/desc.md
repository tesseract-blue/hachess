Author: Hart Traveller

# Goal

First, create a simple Q-learning algorithm which treats each unique board state as a "state". This won't work that well, however, because there are such a massive variety of states in the game of chess that the size of the Q-table would have to grow arbitrarily large in order to actually capture the state space. With that said, first I will implement the algorithm to do this.

Once that is complete, I think the potentially more effective algorithm will be an algorithm which tries to identify more "broad" states, which it is more likely to fall into, and which would be more useful.

Each state could be represented as a collection of actions. For instance:

- there is a fork available here
- there is a pin of the queen on the bishop here
- etc etc

then, given a "state" as a collection of general actions, the agent would select one of the actions from the available states

The next question is whether the algorithm can learn to find "states" - ie: actions which are an effective metric for teaching it

Resources Used:

- https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
- https://github.com/genyrosk/gym-chess
