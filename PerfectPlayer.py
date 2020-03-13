from build.perfect_player import Position, Solver
import numpy as np

class PerfectPlayer:
	def __init__(self, book_dir):
		self.solver = Solver()
		self.solver.loadBook(book_dir)
		self.pos_cache = {}

	def get_position_scores(self, state):
		current_position = self._convert_state(state)

		if current_position in self.pos_cache:
			return self.pos_cache[current_position]

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

		self.pos_cache[current_position] = (scores, *self._position_evaluation(scores))
		return self.pos_cache[current_position]

	def _convert_state(self, actions):			
		return ''.join(map(str, actions[np.nonzero(actions)]))

	def _position_evaluation(self, scores):
		scores = np.array(scores)
		value = np.sign(np.max(scores))
		policy = (scores == scores.max()).astype(int)
		return value, policy/policy.sum()