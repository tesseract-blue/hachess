# resources
# - https://github.com/genyrosk/gym-chess
# https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

import gym, random

from gym_chess import ChessEnvV2

from hachess.common import vprint

env = gym.make("ChessVsSelf-v2")

state = env.state

# select a move and convert it into an action
moves = env.possible_moves
move = random.choice(moves)
action = env.move_to_action(move)

# or select an action directly
actions = env.possible_actions
action = random.choice(actions)

# pass it to the env and get the next state
new_state, reward, done, info = env.step(action)
vprint(reward, done)


# --- QLearning RL Tutorail


# env = gym.make("Taxi-v3", new_step_api=True, render_mode="human")

# env.reset()


# print("Action Space {}".format(env.action_space))
# print("State Space {}".format(env.observation_space))

# --- OPENAI DOCS

# env = gym.make("LunarLander-v2", render_mode="human", new_step_api=True)
# env.action_space.seed(42)

# observation, info = env.reset(seed=42, return_info=True)

# for _ in range(1000):
#     observation, reward, done, trunc, info = env.step(env.action_space.sample())

#     if done:
#         observation, info = env.reset(return_info=True)

# env.close()
