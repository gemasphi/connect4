from build.perfect_player import Position, Solver
import numpy as np
import pdb;

class PerfectPlayer:
	def __init__(self, book_dir):
		self.solver = Solver()
		self.solver.loadBook(book_dir)

	def get_position_scores(self, state):
		current_position = self._convert_state(state)
		scores = []
		for move in range(7):
			pos = Position()
			pos.play(current_position)

			if pos.canPlay(move):
				if pos.isWinningMove(move):
					score = int((pos.WIDTH * pos.HEIGHT + 1 - pos.nbMoves()) / 2)
				else:	
					pos.playCol(move)
					score = self.solver.solve(pos, False)*-1
			else:
				score = -float("inf")

			scores.append(score)

		return scores

	def _convert_state(self, actions):			
		return ''.join(map(str, actions[np.nonzero(actions)]))