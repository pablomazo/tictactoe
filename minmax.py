import numpy as np

class MinMaxAgent:
	def __init__(self, board_class, playerID=1,ab=True):
		'''
		If playerID = 1 agent tries to maximize score, 
		else to minimize
		ab: Use alpha-beta to optimize tree exploration.
		'''
		self.board = board_class
		self.playerID = playerID
		self.ab = ab

	def select_action(self, state, avail_act):
		if self.ab:
			alpha = -100000000
			beta = 100000000
			if self.playerID == 1:
				action, _ = self.maxfunAB(state, alpha, beta)
			else:
				action, _ = self.minfunAB(state, alpha, beta)
			return action
		else:
			if self.playerID == 1:
				action, _ = self.maxfun(state)
			else:
				action, _ = self.minfun(state)
			return action

	def maxfun(self, state):
		turn = self.board.turn
		best_reward = -100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])
			if not self.board.end:
				_, reward = self.minfun(next_state)

			# If reward is higher replace final_action.
			if reward > best_reward:
				final_action = action
				best_reward = reward

			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

		return final_action, best_reward

	def minfun(self, state):
		turn = self.board.turn
		best_reward = +100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])

			if not self.board.end:
				_, reward = self.maxfun(next_state)

			# If reward is higher replace final_action.
			if reward < best_reward:
				final_action = action
				best_reward = reward

			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

		return final_action, best_reward

	def maxfunAB(self, state, alpha, beta):
		#print('state:',state)
		turn = self.board.turn
		best_reward = -100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])

			if not self.board.end:
				_, reward = self.minfunAB(next_state, alpha, beta)
			
			alpha = max(reward, alpha)

			# If reward is higher replace final_action.
			if reward > best_reward:
				final_action = action
				best_reward = reward

			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

			if alpha > beta:
				break

		return final_action, best_reward

	def minfunAB(self, state, alpha, beta):
		turn = self.board.turn
		best_reward = +100000000
		final_action = None

		# Iterate over possible actions:
		for action in self.board.avail_actions(state):
			index = self.board.action2index(action)
			next_state, reward = self.board.play(index[0], index[1])

			if not self.board.end:
				_, reward= self.maxfunAB(next_state, alpha, beta)
			
			beta = min(reward, beta)

			# If reward is higher replace final_action.
			if reward < best_reward:
				final_action = action
				best_reward = reward

			# Reset state
			self.board.turn = turn
			self.board.board[index[0], index[1]] = 0
			self.board.end = False

			if alpha > beta:
				break

		return final_action, best_reward

	def win_message(self):
		print("Well... I'm perfect")