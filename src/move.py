from piece import Piece

class Move:

	def __init__(self, piece, source, des, des_piece = None):
		self.piece = piece
		self.source = source
		self.des = des
		self.des_piece = des_piece

	def __str__(self):
		if (self.des_piece is not None):
			return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des) + " takes " + str(self.des_piece))
		else:
			return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des))

	def __eq__(self, other):
		if not (self.piece == other.piece):
			return False
		if not (self.des_piece == other.des_piece):
			return False
		if (self.source[0] != other.source[0]) or (self.source[1] != other.source[1]):
			return False
		if (self.des[0] != other.des[0]) or (self.des[1] != other.des[1]):
			return False
		return True

	def get_piece(self):
		return self.piece

	def get_source(self):
		return self.source

	def get_des(self):
		return self.des


