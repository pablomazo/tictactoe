import numpy as np

class TicTacToe_Board:
	def __init__(self):
		self.board = np.zeros([3,3])
		self.turn = 1

		self.p1 = 1
		self.p1_symbol = 'x'

		self.p2 = -1
		self.p2_symbol = 'o'

		self.end = False

	def reset(self):
		self.board = np.zeros([3,3])
		self.turn = 1
		self.end = False

	def play(self, i, j):
		# If position is free:
		if self.board[i,j] == 0:
			self.board[i,j] = self.turn

			self.turn = -1 if self.turn == 1 else 1

			# Check if there is a winner after the move:
			winner = self.check_end()

			# Get new state of the game:
			new_state = self.get_state().copy()

			if winner is None:
				# There is no winner:
				return new_state, 0
			elif winner == 1:
				# Player one won:
				return new_state, 100
			elif winner == -1:
				# Player two won:
				return new_state, -1
			elif winner == 0:
				# Drawn
				return new_state, 0

		# If positions is occupied return penalty.
		else:
			new_state = self.get_state().copy()
			return new_state, -10

	def check_end(self):
		for i in range(3):
			# Check columns.
			if np.sum(self.board[i,:]) == 3: 
				self.end = True
				return 1

			if np.sum(self.board[i,:]) == -3: 
				self.end = True
				return -1

			# Check rows.
			if np.sum(self.board[:,i]) == 3: 
				self.end = True
				return 1

			if np.sum(self.board[:,i]) == -3: 
				self.end = True
				return -1

		# Check diagonal.
		diag1 = np.sum([self.board[i,i] for i in range(3)])
		diag2 = np.sum([self.board[i,3-i-1] for i in range(3)])
		diag = max(abs(diag1), abs(diag2))

		if abs(diag) == 3:
			self.end = True

			if diag1 == 3 or diag2 == 3:
				return 1

			else:
				return -1

		# Check if there are available positions.
		if 0 not in self.board:
			self.end = True
			return 0

		# The game did not finish.
		return None

	def get_state(self):
		# Returns a vector with the state of the board:
		return self.board.reshape(9)

	def avail_actions(self, board):
		# Returns the available actions for a given board state..
		actions = []

		# Each action is given as a vector with a one in the free position.
		for ac in range(9):
			if board[ac] == 0:
				actions.append(ac)

		return actions

	def action2index(self, action):
		# Receives an action vector an converts to board indexes.
		act2vec = [[0,0], [0,1], [0,2],\
		           [1,0], [1,1], [1,2],\
		           [2,0], [2,1], [2,2]]

		return act2vec[action]

	def plot(self):
        # p1: x  p2: o
		for i in range(0, 3):
			print('-------------')
			out = '| '
			for j in range(0, 3):
				if self.board[i, j] == 1:
					token = 'x'
				if self.board[i, j] == -1:
					token = 'o'
				if self.board[i, j] == 0:
					token = ' '
				out += token + ' | '
			print(out)
		print('-------------')