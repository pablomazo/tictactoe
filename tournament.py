from board import TicTacToe_Board
from Agent import *
from DQN import DQN
from hard_code import hardcode

# Initialize board to play:
board = TicTacToe_Board()

# Inialize players
policy = DQN(9,105,60,9)
player1 = AIAgent(policy)
player1.load_model('AIagent2.pth')
player2 = AIAgent(policy)
player2.load_model('AIagent2.pth')

NGAMES = 1000

win, drawn, lost = 0, 0, 0
for game in range(NGAMES):
	board.reset()
	state = board.get_state().copy()
	while not board.end:
	
		# Get list of possible actions:
		avail_act = board.avail_actions(state)
	
		# First agent playes
		action = player1.select_action(state, avail_act)
		index = board.action2index(action)
		next_state, _ = board.play(index[0],index[1])
	
		# Second agent playes:
		if not board.end:
			# Update available actions:
			avail_act = board.avail_actions(next_state)
			# Set a minus on "next_state" so AI always sees +1 as its play.
			action2 = player2.select_action(next_state, avail_act)
			index = board.action2index(action2)
			state, _ = board.play(index[0],index[1])

	if board.winner == 1:
		win += 1
	elif board.winner == -1:
		lost += 1
	elif board.winner == 0:
		drawn += 1

print('Win prob:', float(win/NGAMES))
print('Lossing prob:', float(lost/NGAMES))
print('Drawn prob:', float(drawn/NGAMES))