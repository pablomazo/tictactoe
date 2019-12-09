import numpy as np
import random
import torch

class AIAgent:
	def __init__(self, policy, target=None, train=False, playerID=1):
		self.policy = policy
		self.playerID = playerID

		if train:
			self.target = target
			self.GAMMA = 0.99

	def select_action_train(self, state, EPS=0e0):
		# Take an action from random or policy:
		state *= self.playerID

		if random.random() < EPS:
			# Get random action:
			iaction = torch.randint(0,5,(1,1))

		else:
			# Select action from policy:
			policy_value = self.policy(torch.Tensor(state))
			iaction = policy_value.max(0)[1].view(1,1)
		return iaction

	def select_action(self, state, avail_actions):
		# Select action from policy:
		policy_value = self.policy(torch.Tensor(state))
		iaction = policy_value.max(0)[1].view(1,1)
		if iaction.item() not in avail_actions:
			iaction = avail_actions[np.random.randint(0,high=nactions)]

		return iaction

	def load_model(self, file):
		self.policy.load_state_dict(torch.load(file))

	def win_message(self):
		print("I won at TicTacToe. Now I'm ready to conquer the world")

class RandomAgent:
	def select_action(self, state, avail_actions):
		# Take an action from random or policy:
		nactions = len(avail_actions)
		action = avail_actions[np.random.randint(0,high=nactions)]
		return action

	def win_message(self):
		print("C'mon... I'm just playing random...")

class HumanAgent:
	def select_action(self, state, avail_actions):
		# Take an action from random or policy:
		action = 10
		while action not in avail_actions:
			action = np.zeros(9)
			i = int(input('Fila:'))
			j = int(input('Columna:'))
	
			i -= 1
			j -= 1
	
			action = 3*i+j
		return action