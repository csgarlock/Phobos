class TeamInfo:
	def __init__(self, team, board):
		self.board = board
		self.team = team
		self.absolute_pins = []

	def update_from_move(self, move):
		pass