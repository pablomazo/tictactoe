import numpy as np

class MinMaxAgent:
	def __init__(self, board_class, playerID=1):
		'''
		If playerID = 1 agent tries to maximize score, 
		else to minimize
		'''
		self.board = board_class
		self.playerID = playerID

	def select_action(self, state, avail_act):
		if self.playerID == 1:
			action, _ = self.maxfun(state)
		else:
			action, _ = self.minfun(state)

		return action

	def maxfun(self, state):
		#print('state:',state)
		turn = self.board.turn
		best_reward = -100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])
			#print('next_state:',next_state)
			if not self.board.end:
				_, reward = self.minfun(next_state)

			# If reward is higher replace final_action.
			if reward > best_reward:
				final_action = action
				best_reward = reward

			#print(self.board.end)
			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

		return final_action, best_reward

	def minfun(self, state):
		#print('state:',state)
		turn = self.board.turn
		best_reward = +100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])
			#print('next_state:',next_state)
			if not self.board.end:
				_, reward = self.maxfun(next_state)

			# If reward is higher replace final_action.
			if reward < best_reward:
				final_action = action
				best_reward = reward

			#print(self.board.end)
			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

		return final_action, best_reward

	def win_message(self):
		print("Well... I'm perfect")