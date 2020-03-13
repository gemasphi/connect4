from build.perfect_player import Position, Solver
import numpy as np

class PerfectPlayer:
	def __init__(self, book_dir):
		self.solver = Solver()
		self.solver.loadBook(book_dir)
		self.pos_cache = {}

	def get_one_position_score(self, state):
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

	def get_position_scores(self, state):
		print(state)
		if state.ndim > 1:
			score_b, v_b, p_b = [], [], []
			for s in state:
				score, v, p = self.get_one_position_score(s)
				score_b.append(score)
				v_b.append(v)
				p_b.append(p)
			return np.array(score_b), np.array(v_b), np.array(p_b) 
		else:
			score, v, p = self.get_one_position_score(state)
			return np.array([score]), np.array([v]), np.array([p])
		

	def _convert_state(self, actions):			
		return ''.join(map(str, actions[np.nonzero(actions)]))

	def _position_evaluation(self, scores):
		scores = np.array(scores)
		value = np.sign(np.max(scores))
		policy = (scores == scores.max()).astype(int)
		return np.array([value]), np.array(policy/policy.sum())