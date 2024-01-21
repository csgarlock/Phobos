from piece import Piece

class Move:

	def __init__(self, piece, source, des):
		self.piece = piece
		self.source = source
		self.des = des

	def __str__(self):
		return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des))

	def __eq__(self, other):
		if (self.piece != other.piece):
			return False
		if ((self.source[0] != other.source[0]) or ([self.source[1]] != self.source[1])):
			return False
		if ((self.des[0] != other.des[0]) or ([self.des[1]] != self.des[1])):
			return False
		return True

	def get_piece(self):
		return self.piece

	def get_source(self):
		return self.source

	def get_des(self):
		return self.des


